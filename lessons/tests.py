from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lessons.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    # client = APIClient()
    # client.force_authenticate(user=None, token=None)

    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        '''Тестирование создания урока'''
        data = {
            "name": "test",
            "description": "test"
        }

        response = self.client.post('/lessons/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_lesson(self):
        """ Тестирование вывода списка уроков"""
        response = self.client.get('/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_lesson(self):
        """ Тестирование удаления урока"""
        Lesson.objects.create(name="del_test", description= "del_test")
        response = self.client.delete('/lessons/destroy/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        """ Тестирование изменения урока"""
        Lesson.objects.create(name="test", description= "test")
        response = self.client.patch('/lessons/update/3/', {"description": "new_test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

