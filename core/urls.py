from django.urls import path
from .views import HomeView

app_name = 'core_app'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]