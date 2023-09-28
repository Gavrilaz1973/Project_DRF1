import datetime

from celery import shared_task
from config import settings
from users.models import User


def is_active_user():
    user_list = User.objects.filter(is_activ=True)
    for user in user_list:
        date_visit = user.last_login + datetime.timedelta(days=30)
        if datetime.date.today() > date_visit:
            user.is_active = False
            user.save()


