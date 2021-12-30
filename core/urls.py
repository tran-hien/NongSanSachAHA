from django.urls import path

from core.models import Feedback
from . import views

app_name = 'core_app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('contactus/', views.ContactClass.as_view(), name='contacts'),
    path('feedback/', views.FeedbackClass.as_view(), name='feed_back'),
    path('feedback_view/', views.FeedbackViewClass.as_view(), name='fb_view'),
]
