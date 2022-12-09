from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from mobile_re.serializers import MobileInvoiceSerializer, MobileRequestSerializer
from mobile_re.models import MobileInvoice, MobileRequest


class MobileRequestUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MobileRequest.objects.all()
    serializer_class = MobileRequestSerializer


class MobileRequestView(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = MobileRequest.objects.all()
    serializer_class = MobileRequestSerializer


class MobileInvoiceView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = MobileInvoice.objects.all()
    serializer_class = MobileInvoiceSerializer
