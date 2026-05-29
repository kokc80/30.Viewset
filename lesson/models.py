from django.db import models
from users.models import User

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
    descr = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    ),
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец курса",
                              help_text="Укажите владельца курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]

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
    descr = models.TextField(
        verbose_name="Описание", help_text="Введите описание", blank=True, null=True
    )
    video = models.URLField(
        blank=True,
        null=True,
        verbose_name="Видео",
        help_text="Укажите ссылку на видеоурок",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="lessons",
        default=1,
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец урока",
                              help_text="Укажите владельца урока")

class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="оплативший_пользователь"
    )
    payment_date = models.DateField(auto_now_add=True, verbose_name="дата_оплаты")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="оплаченный_курс", null=True
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="оплаченный_урок", null=True
    )
    payment_sum = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(
        choices=[("1", "Наличные"), ("2", "Перевод")],
        verbose_name="способ_оплаты",
        max_length=10,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]

    def __str__(self):
        return f"Урок {self.name}"
