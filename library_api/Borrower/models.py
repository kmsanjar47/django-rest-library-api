from django.db import models
from Branch.models import Branch
from rest_framework import serializers


# Create your models here.
class Borrower(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    membership_date = models.DateTimeField(auto_now_add=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Borrower
