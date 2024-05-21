from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from Loan.models import Loan, LoanSerializer


# Create your views here.
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [AllowAny]
