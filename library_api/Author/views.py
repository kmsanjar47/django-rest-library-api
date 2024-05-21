from django.shortcuts import render
from rest_framework import viewsets
from Author.models import Author, AuthorSerializer
from rest_framework.permissions import AllowAny

# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
