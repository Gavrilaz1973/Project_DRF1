from django.db import models

from config import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='courses/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='студенты', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Subscribe(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f"{self.course} {self.user}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'