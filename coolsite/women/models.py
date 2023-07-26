from django.db import models

# Create your models here.
class Product(models.Model):
    model = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    color = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)