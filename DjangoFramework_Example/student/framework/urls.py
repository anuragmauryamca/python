from django.urls import path
from rest_framework import views

from .views import productlist, product_details

urlpatterns = [
    path('product/', view=productlist, name="productlist"),
    path('product/<int:pk>', view=product_details, name="product_details"),




]
