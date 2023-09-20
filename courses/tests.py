from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Subscribe, Course
from users.models import User


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)
        Course.objects.create(name='test')
    def test_create_subscribe(self):
        """ Тестирование функционала работы подписки на обновления курса"""
        data = {
            "course": 1,
            "user": 1
        }

        response = self.client.post('/courses/subscribe/create/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



