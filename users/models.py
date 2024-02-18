from django.contrib.auth.models import AbstractUser
from django.db import models
from category.models import NULLABLE


class UserRoles(models.TextChoices):
    """ Создание ролей пользователя """
    TEACHER = 'teacher'
    MODERATOR = 'moderator'


class User(AbstractUser):
    """ Отображение пользователей """
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=55, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=55, verbose_name='Город', **NULLABLE)
    roles = models.CharField(max_length=150, choices=UserRoles.choices, default=UserRoles.TEACHER, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
