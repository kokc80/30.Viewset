from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import CoursePay
from users.serializers import UserSerializer, CoursePaySerializer
from users.services import convert_rub_to_usd, create_stripe_price, create_stripe_session


class UserCreateAPIView(CreateAPIView):
    """Разрешения выставлено для всех непосредственно в контролере"""

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Получаем данные из сериализатора без сохранения
        user = serializer.save(is_active=True)
        # Устанавливаем пароль через сериализатор или напрямую
        password = serializer.validated_data.get("password")
        if password:
            user.set_password(password)
            user.save()
        else:
            # Если пароля нет, сохраняем без изменения пароля
            user.save()


class CoursePayCreateAPIView(CreateAPIView):
    """Разрешения выставлено для всех непосредственно в контролере"""

    serializer_class = CoursePaySerializer

    def perform_create(self, serializer):
        payment = serializer.save(pay_user=self.request.user)
        amount_in_dollars = convert_rub_to_usd(payment.amount)
        price = create_stripe_price(amount_in_dollars)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()

