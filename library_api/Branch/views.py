from django.shortcuts import render
from Branch.models import Branch, BranchSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.


class BranchViewset(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [AllowAny]
