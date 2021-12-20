from django.contrib import admin

from product.models import Category, Product, Variation

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Variation)