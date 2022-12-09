from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from mobile_re.serializers import MobileInvoiceSerializer, MobileRequestSerializer
from mobile_re.models import MobileInvoice, MobileRequest


class MobileRequestUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Accept the following PATCH parameters: phone_model,
    problem_desc, status.
    """
    permission_classes = (IsAuthenticated,)
    queryset = MobileRequest.objects.all()
    serializer_class = MobileRequestSerializer


class MobileRequestView(ModelViewSet):
    """
    Accept the following POST parameters: phone_model,
    problem_desc, status, user.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = MobileRequest.objects.all()
    serializer_class = MobileRequestSerializer


class MobileInvoiceUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Accept the following PATCH parameters: price.
    """
    permission_classes = (IsAuthenticated,)
    queryset = MobileInvoice.objects.all()
    serializer_class = MobileInvoiceSerializer


class MobileInvoiceView(ModelViewSet):
    """
    Accept the following POST parameters: mobile_request, price.
    """
    permission_classes = (IsAuthenticated,)
    queryset = MobileInvoice.objects.all()
    serializer_class = MobileInvoiceSerializer
