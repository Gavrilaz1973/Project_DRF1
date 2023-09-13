from django.db import models

from config import settings
from courses.models import Course
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='lessons/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    video = models.TextField(**NULLABLE, verbose_name='Ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='студенты', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


