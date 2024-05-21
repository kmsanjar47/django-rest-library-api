from django.shortcuts import render
from Category.models import Category, CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
