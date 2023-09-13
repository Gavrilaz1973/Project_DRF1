from django.shortcuts import render
from lessons.models import Lesson
from lessons.permissions import IsOwnerOrStaff, IsSuperuser
from lessons.serializers import LessonSerializer, LessonListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsSuperuser]


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer


class LessonDestroyView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsSuperuser]


class LessonRetrieveView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOrStaff]


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOrStaff]


