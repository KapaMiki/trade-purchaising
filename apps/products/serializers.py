from rest_framework.validators import ValidationError, UniqueValidator
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Product
from apps.companies.models import Company
from apps.categories.models import Category
from apps.orders.serializers import OrderSerializer





class ProductSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'count',
                  'price',
                  'avatar',)


class ProductCreateSerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    avatar = serializers.ImageField()

    class Meta:
        model = Product
        fields = ('company_id',
                  'category_id',
                  'name',
                  'description',
                  'count',
                  'price',
                  'avatar',)

    def validate_company_id(self, id):
        company = get_object_or_404(Company, id=id)
        if self.context['request'].user != company.owner:
            return ValidationError("It's not your company")
        return id

    def validate_category_id(self, id):
        category = get_object_or_404(Category, id=id)
        if self.context['request'].user != category.company.owner:
            return ValidationError("It's not your category")
        return id


class ProductUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    class Meta:
        model = Product
        fields = ('name',
                  'description',
                  'count',
                  'price',
                  'avatar',)


class ProductOrdersSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    avatar = serializers.ImageField()

    class Meta:
        model = Product
        fields = ('company_id',
                  'category_id',
                  'name',
                  'description',
                  'count',
                  'price',
                  'avatar',
                  'orders')

    def get_orders(self, obj):
        return OrderSerializer(obj.order_set.all(), many=True).data
