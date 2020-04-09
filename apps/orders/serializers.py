from rest_framework import serializers
from .models import Order



class OrderSerializer(serializers.ModelSerializer):
    product_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id',
                  'status',
                  'user',
                  'product',
                  'count',
                  'price',
                  'product_price',)

    def get_product_price(self, obj):
        return obj.product.price