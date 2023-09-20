from django.urls import path

from courses.apps import CourseConfig
from courses.views import CourseViewSet, SubscribeListView, SubscribeCreateView, SubscribeUpdateView, \
    SubscribeRetrieveView, SubscribeDestroyView
from rest_framework.routers import DefaultRouter

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='courses')

urlpatterns = [
    path('subscribe/', SubscribeListView.as_view(), name='subscribe_list'),
    path('subscribe/create/', SubscribeCreateView.as_view(), name='subscribe_create'),
    path('subscribe/update/<int:pk>/', SubscribeUpdateView.as_view(), name='subscribe_update'),
    path('subscribe/retrieve/<int:pk>/', SubscribeRetrieveView.as_view(), name='subscribe_retrieve'),
    path('subscribe/destroy/<int:pk>/', SubscribeDestroyView.as_view(), name='Subscribe_destroy'),
    ]+router.urls