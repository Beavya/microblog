from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdvUser, Post, Comment

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2')

class ChangeUserInfoForm(forms.ModelForm):
    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'avatar', 'bio')
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'avatar': 'Аватар',
            'bio': 'О себе',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'Заголовок',
            'content': 'Текст поста',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Ваш комментарий'}
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }