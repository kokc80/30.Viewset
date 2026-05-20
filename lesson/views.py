from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from lesson.models import Course, Lesson
from lesson.serializer import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet): #Dog
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateApiView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListApiView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveApiView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateApiView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDestroyApiView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
