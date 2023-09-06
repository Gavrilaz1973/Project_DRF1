from courses.apps import CourseConfig
from courses.views import CourseViewSet
from rest_framework.routers import DefaultRouter

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='courses')

urlpatterns = router.urls