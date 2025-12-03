# main/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.RegisterUserView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
]