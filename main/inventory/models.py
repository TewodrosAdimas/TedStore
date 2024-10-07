from django.db import models
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.quantity < 0:
            raise ValidationError('Quantity cannot be negative.')
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')

    def __str__(self):
        return self.name
