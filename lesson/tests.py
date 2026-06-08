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
        #  спросить как сравнивать?
        # self.assertEqual(data.get("course"), self.lesson.course)

    def test_lesson_create(self):
        url = reverse("lessons:lessons_create")
        course_t = self.course
        data = {
            "name": "Тестовый урок",
            "descr": "Описание",
            "course": "Тестовый курс",
            "owner": self.user
        }

        response =self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



# Create your tests here.
