from rest_framework.fields import SerializerMethodField
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer
from lesson.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_count_on_course=SerializerMethodField()

    def get_lesson_count_on_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "descr", "lesson_count_on_course")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
