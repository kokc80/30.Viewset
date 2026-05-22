from django.urls import path
from rest_framework.routers import SimpleRouter

from lesson.apps import LessonConfig
from lesson.views import (CourseViewSet, LessonListApiView, LessonCreateApiView, LessonRetrieveApiView,
                          LessonUpdateApiView, LessonDestroyApiView )

app_name = LessonConfig.name
router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/destroy/", LessonDestroyApiView.as_view(), name="lessons_delete"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lessons_update"),
]

urlpatterns += router.urls
