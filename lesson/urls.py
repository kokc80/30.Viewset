from django.urls import path
from rest_framework.routers import SimpleRouter

from lesson.apps import LessonConfig
from lesson.views import (CourseViewSet, CourseCreateApiView,
                       CourseDestroyApiView, CourseListApiView,
                       CourseRetrieveApiView, CourseUpdateApiView)

app_name = LessonConfig.name
router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("courses/", CourseListApiView.as_view(), name="courses_list"),
    path("courses/<int:pk>/", CourseRetrieveApiView.as_view(), name="courses_retrieve"),
    path("courses/create/", CourseCreateApiView.as_view(), name="courses_create"),
    path(
        "courses/<int:pk>/destroy/",
        CourseDestroyApiView.as_view(),
        name="courses_delete",
    ),
    path(
        "courses/<int:pk>/update/", CourseUpdateApiView.as_view(), name="courses_update"
    ),
]

urlpatterns += router.urls
