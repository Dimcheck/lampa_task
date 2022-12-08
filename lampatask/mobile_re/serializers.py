from rest_framework import serializers

from mobile_re.models import MobileInvoice, MobileRequest


class MobileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileRequest
        fields = '__all__'


class MobileInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileInvoice
        fields = '__all__'
