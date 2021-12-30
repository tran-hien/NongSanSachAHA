from order.models import Order
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'address', 'city',  'credit_card']
