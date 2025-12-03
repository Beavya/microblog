from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from .forms import ChangeUserInfoForm
from .models import AdvUser
from django.views.generic import DeleteView
from django.contrib import messages


def index(request):
    return render(request, 'main/index.html')

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:login')

@login_required
def profile(request):
    return render(request, 'main/profile.html')

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    form_class = ChangeUserInfoForm
    template_name = 'main/change_user_info.html'
    success_message = 'Данные успешно изменены.'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('main:profile')

class DeleteUserView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')
    success_message = 'Ваш профиль успешно удалён.'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        from django.contrib.auth import logout
        logout(request)
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response