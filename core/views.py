from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class ContactClass(TemplateView):
    template_name="core/contacts.html"