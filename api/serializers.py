from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'product_price', 'available_product_stock')


class PurchaseSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseSerializertest(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'