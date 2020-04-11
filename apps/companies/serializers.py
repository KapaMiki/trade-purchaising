from rest_framework.validators import ValidationError, UniqueValidator
from rest_framework import serializers
from .models import Company
from apps.categories.serializers import CategorySerializer
from apps.products.serializers import ProductOrdersSerializer




class CompanySerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    photo = serializers.ImageField()

    class Meta:
        model = Company
        fields = ('id',
                  'owner',
                  'name',
                  'description',
                  'created_data',
                  'BIN',
                  'activity',
                  'photo',
                  'country',
                  'city',
                  'categories')

    def get_categories(self, obj):
        return CategorySerializer(obj.category_set.all(), many=True).data


class CompanyCreateUpdateSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()

    class Meta:
        model = Company
        fields = ('name',
                  'description',
                  'created_data',
                  'BIN',
                  'activity',
                  'photo',
                  'country',
                  'city')


# class CompanyOrdersSerializer(serializers.ModelSerializer):
#     products = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Company
#         fields = ('name',
#                   'description',
#                   'created_data',
#                   'BIN',
#                   'activity',
#                   'photo',
#                   'country',
#                   'city')
#
#     def get_products(self, obj):
#         return ProductOrdersSerializer(obj.product_set.all(), many=True)



