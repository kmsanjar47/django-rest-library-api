from django.db import models
from rest_framework import serializers
from Author.models import Author
from Publisher.models import Publisher
from Category.models import Category
from Branch.models import Branch


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    summery = models.CharField(max_length=500, null=True, blank=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book
