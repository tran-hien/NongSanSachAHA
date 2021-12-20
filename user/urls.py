from django.urls import path
from . import views

app_name = 'user_app'
urlpatterns = [
    path('login/', views.LoginClass.as_view(), name='login'),
    path('profile/', views.LoginSuccessClass.as_view(), name='loginsuccess'),
    path('register/', views.RegisterClass.as_view(), name='register'),
    path('register/registed', views.RegisterSuccessClass.as_view(), name='registed'),
    path('logout/', views.LogoutClass.as_view(), name='logged_out'),
]