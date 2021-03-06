from django.contrib import admin
from order.models import Order, OrderItem
# Register your models here.

class OrderItemTabuler(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['product', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price', 'phone_number',
                    'address', 'credit_card', 'city', 'status', 'paid']
    list_filter = ['paid', 'created', 'status']
    raw_id_fields = ['user']
    list_editable = ['status', 'paid']
    inlines = [OrderItemTabuler]
    list_per_page = 24
