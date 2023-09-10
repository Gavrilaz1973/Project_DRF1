from courses.models import Course
from courses.serializers import CourseSerializer, CourseDetailSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer



