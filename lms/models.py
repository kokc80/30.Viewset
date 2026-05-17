from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="lms/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Введите превью",
    )
    descr = models.TextField(verbose_name="Описание", help_text="Введите описание")


class Lesson(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="lms/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Введите превью",
    )
    descr = models.TextField(verbose_name="Описание", help_text="Введите описание")
    video = models.URLField( blank=True, null=True, verbose_name="Видео")