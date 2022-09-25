
from django.urls import path
from .views import (
    ProductAPIView,
    ProductUpdateDeleteAPIView,
    CategoryAPIView,
    CategoryUpdateDeleteAPIView,
    ProductImagesAPIView,
    ProductImagesUpdateDeleteAPIView
)

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductUpdateDeleteAPIView.as_view(), name="product_get_or_update"),

    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryUpdateDeleteAPIView.as_view(), name="categories_get_or_update"),

    path('product_imgs/', ProductImagesAPIView.as_view(), name='product_imgs'),
    path('product_imgs/<int:pk>/', ProductImagesUpdateDeleteAPIView.as_view(), name="product_imgs_get_or_update"),

]