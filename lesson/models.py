from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="lesson/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Введите превью",
    )
    descr = models.TextField(blank=True, null=True, verbose_name="Описание", help_text="Введите описание")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['name']

    def __str__(self):
        return f"Курс {self.name}"


# к урокам привязаны курсы
class Lesson(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    preview = models.ImageField(
        upload_to="lesson/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Введите превью",
    )
    descr = models.TextField(verbose_name="Описание", help_text="Введите описание", blank=True, null=True)
    video = models.URLField(blank=True, null=True, verbose_name="Видео", help_text="Укажите ссылку на видеоурок")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="lessons", default=1)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['name']

    def __str__(self):
        return f"Урок {self.name}"

