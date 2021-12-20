from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, default=0)
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)