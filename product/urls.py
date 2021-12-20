from django.urls import path
from . import views

app_name = 'product_app'
urlpatterns = [
    path('product/', views.ProductClass.as_view(), name='product'),
    path('product/<int:product_id>/', views.ProductDetail.as_view(), name='details'),
]