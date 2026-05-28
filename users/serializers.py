from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from users.models import Payment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Укажите нужные поля


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
