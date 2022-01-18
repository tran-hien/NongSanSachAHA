from pprint import pprint
from re import template
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView

import user

# Create your views here.

class LoginClass(LoginView):
    template_name = 'Login/login.html'

class LoginSuccessClass(LoginRequiredMixin, TemplateView):
    template_name = 'Login/loginsuccess.html'


class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "email",)
        field_classes = {'username': UsernameField}

class RegisterClass(FormView):
    template_name = 'Register/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'], 
            password=data['password1'],
            email=data['email']
        )
        url = f"{reverse('user_app:registed')}?username={new_user.username}"
        return redirect(url)

class RegisterSuccessClass(TemplateView):
    template_name = 'Register/registersuccess.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context

class LogoutClass(LogoutView):
    template_name = 'Logout/logout.html'