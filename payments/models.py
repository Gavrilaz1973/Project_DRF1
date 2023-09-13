from django.db import models

from courses.models import Course
from lessons.models import Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    METHOD_CHOICES = [('transfer', 'Перевод на счет'), ('cash', 'Наличные'),]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    pay_date = models.DateField(verbose_name='Дата оплаты')
    pay_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    money = models.IntegerField(verbose_name='Оплаченная сумма')
    pay_method = models.CharField(choices=METHOD_CHOICES, default=METHOD_CHOICES[0],
                              verbose_name='Способ оплаты')

    def __str__(self):
        return f"{self.money}"

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'


