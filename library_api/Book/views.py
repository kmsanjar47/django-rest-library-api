from django.shortcuts import render
from rest_framework import viewsets
from Book.models import Book, BookSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        response = Book.objects.all()
        serialized_response = BookSerializer(response, many=True)
        return Response(serialized_response.data)
