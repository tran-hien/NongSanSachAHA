from django.db import models
from django.utils.translation import activate

# Create your models here.

class Category(models.Model):
    title = models.CharField(default='', max_length=100)
    #slug = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    price = models.IntegerField(default='')
    active = models.BooleanField(default=True)
    product_img = models.ImageField(upload_to="product_images/%y", null=True, blank=True)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    price = models.IntegerField(default='')
    sale_price = models.IntegerField(default='')
    inventory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

