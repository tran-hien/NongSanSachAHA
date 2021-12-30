from django.urls import path
from . import views

app_name = 'order_app'
urlpatterns = [
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('my_order/', views.MyOrders.as_view(), name='my_orders'),
    path('order_details/<int:pk>/', views.OrderDetails.as_view(), name='order_details'),
    path('invoice/<int:pk>/', views.OrderInvoice.as_view(), name='invoice'),
]
