from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer



class ProductAPIView(generics.ListCreateAPIView):
    """_summary_

    Args:
        generics (_ProductAPIView_):  _anyone can create product and get the product  permission access to everyone __
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]



class ProductUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """_summary_

    Args:
        generics (_ProductUpdateDeleteAPIView_): _anyone can update product and delete the product  permission access to everyone __
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    

class CategoryAPIView(generics.ListCreateAPIView):
    """_summary_

    Args:
        generics (_CategoryAPIView_): _anyone can create category and get the product category permission access to everyone _
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]



class CategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """_summary_

    Args:
        generics (_CategoryUpdateDeleteAPIView_): _update the product category delete product category_
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ProductImagesAPIView(generics.ListCreateAPIView):

    """_summary_

    Args:
        generics (_ProductImagesAPIView_): _create  the product image get the product image_
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.AllowAny]




class ProductImagesUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):

    """_summary_
    generics (_ProductImagesUpdateDeleteAPIView_): _update the product images delete product images_

    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.AllowAny]