from rest_framework.validators import ValidationError, UniqueValidator
from rest_framework import serializers
from .models import Category
from apps.products.serializers import ProductSerializer
from apps.companies.models import Company
from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError





class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'products')

    def get_products(self, obj):
        return ProductSerializer(obj.product_set.all(), many=True).data


class CategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class CategoryCreateSerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('name',
                  'company_id')

    def validate_company_id(self, id):
        company = get_object_or_404(Company, id=id)
        if self.context['request'].user != company.owner:
            return ValidationError("It's not your company")
        return id

