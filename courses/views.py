from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from courses.models import Course
from courses.paginators import CoursePaginator
from courses.serializers import CourseDetailSerializer, CourseSerializer
from rest_framework.viewsets import ModelViewSet

from lessons.permissions import IsSuperuser, IsOwnerOrStaff


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

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

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CourseDetailSerializer(user)
        return Response(serializer.data)








