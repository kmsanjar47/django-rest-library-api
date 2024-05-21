from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from Publisher.models import Publisher, PublisherSeralizer


# Create your views here.
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSeralizer
    permission_classes = [AllowAny]
