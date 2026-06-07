from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lesson.models import Course, Lesson, Payment
from lesson.validators import LinkYT


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count_on_course = SerializerMethodField()

    def get_lesson_count_on_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "descr", "lesson_count_on_course", "video")


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    video = serializers.CharField(validators=[LinkYT()])

    class Meta:
        model = Lesson
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"
