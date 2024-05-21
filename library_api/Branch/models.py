from django.db import models
from rest_framework import serializers


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Branch
