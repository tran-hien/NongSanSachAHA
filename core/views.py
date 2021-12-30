from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from core.forms import FeedbackForm
from .models import Feedback

#from product import models
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class ContactClass(TemplateView):
    template_name="core/contacts.html"

class FeedbackClass(LoginRequiredMixin, TemplateView):
    form_class = FeedbackForm
    template_name="core/feedback.html"

    def get(self, request):
        feedbackForm=FeedbackForm()
        return render(request, 'core/feedback.html', {'f':feedbackForm})

    def post(self, request):
        feedbackForm=FeedbackForm()
        if request.method == 'POST':
            feedbackForm = FeedbackForm(request.POST)
            if feedbackForm.is_valid():
                feedbackForm.save()
                return render(request, 'core/fb_sent.html')
        return render(request, 'core/feedback.html', {'f':feedbackForm})

class FeedbackViewClass(TemplateView):
    template_name = 'core/feedback_view.html'

    def get(self, request):
        feedbacks_list=Feedback.objects.all()
        context = {'feedbacks':feedbacks_list}
        return render(request,'core/feedback_view.html', context)
