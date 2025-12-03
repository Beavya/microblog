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
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/delete/', views.DeleteUserView.as_view(), name='profile_delete'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]


