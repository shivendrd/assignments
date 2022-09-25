from rest_framework import serializers
from .models import Category, Product, ProductImage
from django.core.exceptions import ValidationError






class CategorySerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_CategorySerializer_): _serializer return category name_
    
    
    Returns:
        _type_: _serialized_object_

    """

    class Meta:
        model = Category
        verbose_name = "category"
        fields = ["name"]






class ProductImageSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_ProductImageSerializer_): _multiple product images can be uploaded in here _
    
    Returns:
        _type_: _serialized_object_
    """
    class Meta:
        model = ProductImage
        verbose_name ="product_image"
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_ProductSerializer_): _product model field are used in this serializers_

    Returns:
        _type_: _serialized_object_
    """
    category = CategorySerializer(read_only=True)
    image = ProductImageSerializer(read_only=True)  
    
    class Meta:
        model = Product
        verbose_name = "product"
        fields = ['name', 'product_sku', 'regular_price','discount_price','is_active', 'weight', 'short_description', 'long_description', 'stock', 'category', 'image']

    def create(self, validated_data):
        return super().create(validated_data)
