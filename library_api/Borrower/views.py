from django.shortcuts import render
from Borrower.models import Borrower, BorrowerSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# Create your views here.
class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    permission_classes = [AllowAny]
