from django.contrib import admin

from lesson.models import Course, Lesson
from users.models import Payment, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "is_superuser",
        "is_active",
        "is_staff",
        "date_joined",
    )
    search_fields = ("email",)


@admin.register(Payment)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "payment_date",
        "course",
        "lesson",
        "payment_sum",
        "payment_method",
    )
    search_fields = ("user",)


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "descr", "video", "course")
    search_fields = ("name",)


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "descr")
    search_fields = ("name",)
