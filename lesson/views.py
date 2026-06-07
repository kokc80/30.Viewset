from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from lesson.models import Course, Lesson, Payment, SubscriptionCourse
from lesson.serializer import (
    CourseDetailSerializer,
    CourseSerializer,
    LessonSerializer,
    PaymentSerializer,
)
from users import permissions
from users.permissions import IsModer, IsNotModer, IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response


class CourseViewSet(
    ModelViewSet
):  # для курса ViewSet классы http://127.0.0.1:8000/course/1/ вывод количества уроков на курсе
    queryset = Course.objects.all()  # нужен для роутер

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        else:
            return CourseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_permissions(self):
    #     if self.action == "create":
    #         permission_classes = [IsAuthenticated]
    #     elif self.action in ["update", "retrieve"]:
    #         permission_classes = [IsModer | IsOwner]
    #     elif self.action == "destroy":
    #         permission_classes = [IsNotModer, IsOwner]
    #     return [permission() for permission in permission_classes]
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated]

        elif self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]

        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsModer | IsOwner]

        elif self.action == "destroy":
            permission_classes = [IsNotModer & IsOwner]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

class LessonCreateApiView(CreateAPIView):  # для Lesson Generic классы
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="moder").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.has_perm("app.can_moderate"):  # замените на ваше условие для модератора
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="moder").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)


class LessonDestroyApiView(DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="moders").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = (
        "course",
        "lesson",
        "payment_method",
    )
    ordering_fields = ("payment_date",)


class SubscriptionCourseAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = SubscriptionCourse.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
        else:
            SubscriptionCourse.objects.create(user=user, course=course_item)
            message = "подписка добавлена"
        return Response({"message": message})

    permission_classes = [IsAuthenticated]

