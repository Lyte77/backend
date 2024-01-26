from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers

# Create your views here.
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
