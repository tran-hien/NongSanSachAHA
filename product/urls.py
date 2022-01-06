from django.urls import path
from . import views

app_name = 'product_app'
urlpatterns = [
    path('product/', views.ProductClass.as_view(), name='product'),
    path('product/<int:product_id>/', views.ProductDetail.as_view(), name='details'),
    path('search/', views.search, name='search'),
    path('freshfruit/', views.freshfruit, name='freshfruit'),
    path('drinkfruit/', views.drinkfruit, name='drinkfruit'),
    path('driedfruit/', views.driedfruit, name='driedfruit'),
    path('vegetable/', views.vegetable, name='vegetable'),
]