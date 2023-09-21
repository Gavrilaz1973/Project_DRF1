from rest_framework import serializers

from payments.models import Payment
from payments.services import session_payment


class PaymentSerializer(serializers.ModelSerializer):
    url_payment = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    def get_url_payment(self, obj):
        pay_crs = obj.pay_course
        pay_mn = obj.money
        return session_payment(pay_crs)
