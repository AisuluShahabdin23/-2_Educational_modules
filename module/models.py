from django.db import models
from category.models import NULLABLE, Category
from users.models import User


class Module(models.Model):
    """ Отображение образовательных модулей """
    title = models.CharField(max_length=100, verbose_name='Название образовательного модуля')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='educational_modules/', verbose_name='Фото', **NULLABLE)
    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", **NULLABLE)
    id_users = models.ManyToManyField(User, verbose_name="Пользователь", related_name='id_users', **NULLABLE)
    count_view = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'
