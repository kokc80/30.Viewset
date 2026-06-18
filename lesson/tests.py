from idlelib.rpc import response_queue

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from lesson.models import Course, Lesson


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email = "su@admin.ru")
        self.course = Course.objects.create(name = "Тестовый курс", descr = "Описание тестового курса")
        self.lesson = Lesson.objects.create(name = "Тестовый урок", course = self.course, owner = self.user, descr = "описание")
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lessons:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("lessons:lessons_create")
        data = {
            "name": "Тестовый урок",
            "descr": "Описание",
            "course": self.course.pk,
            "video": "http://www.youtube.com/watch?v=xh4AyiP6YYs",
            "owner": self.user.pk
        }
        response = self.client.post(url, data)
        # print("Ошибка create",response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lessons:lessons_update", args=(self.lesson.pk,))
        data = {"name" : "Тестовый урок обн"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Тестовый урок обн")

    def test_lesson_delete(self):
        url = reverse("lessons:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lessons:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {'id': self.lesson.id,
                     'course':
                         {'id': self.course.pk,
                          'name': self.course.name,
                          'preview': None,
                          'descr': self.course.descr,
                          'owner': None
                          },
                     'video': self.lesson.video,
                     'name': self.lesson.name,
                     'preview': None,
                     'descr': self.lesson.descr,
                     'owner': self.user.pk
                     }
                ]
        }
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
