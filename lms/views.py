from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from lms.models import Course
from lms.serializer import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Create your views here.
