from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from mobile_re.serializers import MobileInvoiceSerializer, MobileRequestSerializer
from mobile_re.models import MobileInvoice, MobileRequest


class MobileRequestView(ModelViewSet):
    queryset = MobileRequest.objects.all()
    serializer_class = MobileRequestSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class MobileInvoiceView(ModelViewSet):
    queryset = MobileInvoice.objects.all()
    serializer_class = MobileInvoiceSerializer
