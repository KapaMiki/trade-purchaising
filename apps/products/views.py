from .models import Product
from .permissions import IsOwnerCompany, IsOwnCategory
from apps.companies.models import Company
from apps.categories.models import Category
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer
)
from apps.companies.serializers import CompanySerializer




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'create':
            serializer_class = ProductCreateSerializer
        elif self.action == 'update':
            serializer_class = ProductUpdateSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'update':
            permission_classes = [IsAuthenticated, IsOwnerCompany]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsOwnerCompany, IsOwnCategory]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def update(self, request, pk, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        instance = self.get_object()
        serializer = serializer_class(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        comapny_serializer = CompanySerializer(instance.company)
        return Response(status=status.HTTP_202_ACCEPTED, data=comapny_serializer.data)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        company = Company.objects.get(id=serializer.data['company_id'])
        category = Category.objects.get(id=serializer.data['category_id'])
        Product.objects.create(company=company, category=category, **serializer.validated_data)
        comapny_serializer = CompanySerializer(company)
        return Response(status=status.HTTP_201_CREATED, data=comapny_serializer.data)









