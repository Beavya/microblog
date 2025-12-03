from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdvUser

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2')

class ChangeUserInfoForm(forms.ModelForm):
    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'avatar', 'bio')  # ← убрали first_name и last_name
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'avatar': 'Аватар',
            'bio': 'О себе',
        }