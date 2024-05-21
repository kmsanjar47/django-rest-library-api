from django.db import models
from rest_framework import serializers
from Book.models import Book
from Borrower.models import Borrower
from Branch.models import Branch

# Create your models here.
status_choices = [(0, "ON_LOAN"), (1, "RETURNED"), (2, "OVERDUE")]


class Loan(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_id = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    load_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False)
    return_date = models.DateTimeField(null=False)
    status = models.CharField(max_length=20, choices=status_choices)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Loan
