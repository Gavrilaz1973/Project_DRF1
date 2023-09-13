from courses.models import Course
from courses.serializers import CourseSerializer, CourseDetailSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from lessons.permissions import IsSuperuser, IsOwnerOrStaff


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsSuperuser]
        elif self.action == 'destroy':
            self.permission_classes = [IsSuperuser]
        elif self.action == 'update':
            self.permission_classes = [IsOwnerOrStaff]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]







