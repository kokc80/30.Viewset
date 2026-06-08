from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from lesson.models import Course, Lesson



class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email = "su@admin.ru")
        self.course = Course.objects.create(name = "Тестовый курс", descr = "Описание тестового курса")
        self.lesson = Lesson.objects.create(name = "Тестовый урок", course = self.course, owner = self.user, descr = "описание")
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("lessons:course-retrieve", args=(self.course.pk,))
        response = self.client(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)



# Create your tests here.
