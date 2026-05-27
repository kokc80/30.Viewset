from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db import  models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from lesson.models import Course
from users.models import User


# Create your views here.
class Payment(ModelViewSet):
    queryset = User.objects.all()
    filter_backends =  [DjangoFilterBackend,filters.OrderingFilter]
    fiterset_fields = ["course", "lesson", ]
    ordering_fields = ("payment_sum",)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Пользователь"),
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата_оплаты'),
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE).
    payment_sum = models.DecimalField(max_digits=6, decimal_places=2),
    payment_method = models.CharField(choices=[('1', 'Наличные'), ('2', 'Перевод')], verbose_name='способ_оплаты',
                                      max_length=10)
