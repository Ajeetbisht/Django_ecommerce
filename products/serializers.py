from rest_framework import serializers
from .models import *

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizevariant
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    quantity = QuantitySerializer()
    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ['id']
