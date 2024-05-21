from django.db import models
from rest_framework import serializers


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(auto_now=False, null=True)
    date_of_death = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.last_name


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
