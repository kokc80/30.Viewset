from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserSerializer
#     # queryset = User.objects.all() для create не нужен
#     permission_classes = [AllowAny]
#     def perform_create(self, serializer):
#         user = serializer.save(is_active=True)
#         user.set_password(user.password)
#         user.save()



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
