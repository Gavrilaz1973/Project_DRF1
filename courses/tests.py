from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Subscribe, Course
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.pro')
        users = [self.user, ]
        self.course = Course.objects.create(name="test", user=users)
        self.subscribe = Subscribe.objects.create(course=self.course, user=self.user)

    def test_get_retrieve(self):
        """ Тестирование функционала работы подписки на обновления курса"""
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



