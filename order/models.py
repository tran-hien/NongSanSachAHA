from django.db import models
from django.conf import settings
from product.models import Product
from django.shortcuts import reverse
from django.contrib.auth.models import User



# Create your models here.

choices = (
    ('Pending', 'Pending'),
    ('Packed', 'Packed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    phone_number = models.CharField(default=0, max_length=15)
    address = models.CharField(default=0,max_length=150, blank=False, null=False)
    city = models.CharField(max_length=50, default=0)
    credit_card = models.CharField(max_length=10, default=0)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=choices, max_length=10, default='Pending')
    total_price = models.FloatField(null=False, blank=False, default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_absolute_url(self):
        return reverse('order_app:invoice', kwargs={'pk': self.pk})


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='ordered', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'Order Item {self.id}'

'''
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
'''