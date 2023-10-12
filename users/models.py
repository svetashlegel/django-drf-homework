from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    role = models.CharField(max_length=15, verbose_name='роль', **NULLABLE)
    last_login = models.DateTimeField(verbose_name='дата последнего входа', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
