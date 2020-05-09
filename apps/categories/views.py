from .models import Category
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.products.permissions import IsOwnerCompany
from apps.companies.models import Company
from .serializers import (
    CategorySerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer
)
from apps.companies.serializers import CompanySerializer




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'create':
            serializer_class = CategoryCreateSerializer
        elif self.action == 'update':
            serializer_class = CategoryUpdateSerializer
        return serializer_class

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerCompany]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def update(self, request, pk, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        instance = self.get_object()
        serializer = serializer_class(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED, data=serializer.validated_data)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        company = Company.objects.get(id=serializer.data['company_id'])
        Category.objects.create(company=company, **serializer.validated_data)
        company_serializer = CompanySerializer(company)
        return Response(status=status.HTTP_201_CREATED, data=company_serializer.data)