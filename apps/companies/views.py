from .models import Company
from .permissions import IsOwnerCompany, IsBusinessman
from apps.categories.serializers import CategorySerializer
from apps.products.serializers import ProductOrdersSerializer, ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import CompanySerializer, CompanyCreateUpdateSerializer
from rest_framework.decorators import action




class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action in ['update', 'create']:
            serializer_class = CompanyCreateUpdateSerializer
        if self.action in ['categories']:
            serializer_class = CategorySerializer
        if self.action == 'orders':
            serializer_class = ProductOrdersSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'update':
            permission_classes = [IsAuthenticated, IsBusinessman, IsOwnerCompany]
        elif self.action in ['create', 'my']:
            permission_classes = [IsAuthenticated, IsBusinessman]
        elif self.action == 'orders':
            permission_classes = [IsAuthenticated, IsBusinessman, IsOwnerCompany]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(Company.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def update(self, request, pk, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        instance = self.get_object()
        serializer = serializer_class(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if serializer.validated_data.get('photo'):
            serializer.validated_data['photo'] = instance.photo.url
            
        return Response(status=status.HTTP_202_ACCEPTED, data=serializer.validated_data)

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer_class = self.get_serializer_class()
        if user.is_businessman == 0:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message':'User is not businessman'})
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = Company.objects.create(owner=user, **serializer.validated_data)
        serializer.validated_data['photo'] = company.photo.url
        return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)

    def categories(self, request, pk, *args, **kwargs):
        company = get_object_or_404(Company, pk=pk)
        categories = company.category_set.all()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def orders(self, request, pk, *args, **kwargs):
        company = get_object_or_404(Company, pk=pk)
        if request.user == company.owner:
            products = company.product_set.all()
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(products, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN, data={
            'detail':'It is not your Company'
        })

    def my(self, request):
        serializer = self.serializer_class(request.user.company_set.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def products(self, request, pk, *args, **kwargs):
        company = get_object_or_404(Company, pk=pk)
        products = company.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
