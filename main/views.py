from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm

def index(request):
    return render(request, 'main/index.html')

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:login')