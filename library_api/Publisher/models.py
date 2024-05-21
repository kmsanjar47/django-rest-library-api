from django.db import models
from rest_framework import serializers


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, null=False)
    website = models.URLField(max_length=100, null=False)

    def __str__(self):
        return self.name


class PublisherSeralizer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Publisher
