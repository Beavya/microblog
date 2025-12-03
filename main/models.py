# main/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class AdvUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Информация о себе'
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'