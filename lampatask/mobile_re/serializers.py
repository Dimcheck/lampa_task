from rest_framework import serializers

from mobile_re.models import MobileInvoice, MobileRequest


class MobileInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileInvoice
        fields = '__all__'


class MobileRequestSerializer(serializers.ModelSerializer):
    mobile = MobileInvoiceSerializer(many=False)

    class Meta:
        model = MobileRequest
        fields = '__all__'
