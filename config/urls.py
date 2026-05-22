from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("lesson.urls", namespace="lessons")),
    path("admin/", admin.site.urls),
    path("lessons/", include("lesson.urls", namespace="lessons")),
]
