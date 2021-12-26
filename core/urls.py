from django.urls import path
from . import views

app_name = 'core_app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('contactus/', views.ContactClass.as_view(), name='contacts'),
]