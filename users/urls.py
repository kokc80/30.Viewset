from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("payment_list/", PaymentListAPIView.as_view(), name="payment_list"),
] + router.urls
