from payments.apps import PaymentsConfig
from rest_framework.routers import DefaultRouter

from payments.views import PaymentViewSet

app_name = PaymentsConfig.name

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='courses')

urlpatterns = router.urls