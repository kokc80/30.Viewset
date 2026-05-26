from django.core.management.base import BaseCommand
from users.models import Payment, User, Course, Lesson
from datetime import date

class Command(BaseCommand):
    help = "Заполнение таблицы Payment"
    def handle(self, *args, **kwargs):
        # Удаляем существующие записи по оплате
        Payment.objects.all().delete()
        # User.objects.all().delete() # пользователей оставляю
        users = User.objects.all()

        for user in users:
            if user.id % 2 == 0:  # ID пользователя четный
                payment_method = 1
                amount = 500
                course = Course.objects.get(id=1)
                lesson = None
            else:
                payment_method = 2
                amount = 100
                course = None
                lesson = Lesson.objects.get(id=1)

            Payment.objects.create(
                user=user,
                payment_date=date.today(),
                payment_sum=amount,
                payment_method=payment_method,
                course=course,
                lesson=lesson
            )