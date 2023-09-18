from django.shortcuts import render
from rest_framework.permissions import AllowAny

from lessons.models import Lesson
from lessons.paginators import LessonPaginator
from lessons.permissions import IsOwnerOrStaff, IsSuperuser
from lessons.serializers import LessonSerializer, LessonListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny] #[IsSuperuser]


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    pagination_class = LessonPaginator


class LessonDestroyView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]#[IsSuperuser]


class LessonRetrieveView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOrStaff]


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]#[IsOwnerOrStaff]


