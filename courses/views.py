from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, \
    UpdateAPIView
from rest_framework.response import Response

from courses.models import Course, Subscribe
from courses.paginators import CoursePaginator
from courses.serializers import CourseDetailSerializer, CourseSerializer, SubscribeSerializer
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


class SubscribeCreateView(CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [IsSuperuser]


class SubscribeListView(ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    # permission_classes = [IsSuperuser]


class SubscribeDestroyView(DestroyAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [IsSuperuser]


class SubscribeRetrieveView(RetrieveAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [IsOwnerOrStaff]


class SubscribeUpdateView(UpdateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [IsOwnerOrStaff]




