from django.shortcuts import render
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mobile_re.models import MobileInvoice, MobileRequest
from mobile_re.serializers import (MobileInvoiceSerializer,
                                   MobileRequestSerializer)


class MobileRequestUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Accept the following PATCH parameters: phone_model,
    problem_desc, status.
    """
    permission_classes = (IsAuthenticated,)
    queryset = MobileRequest.objects.all()
    serializer_class = MobileRequestSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 'in progress':
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "Cant delete with status: in progress"}
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MobileRequestView(ModelViewSet):
    """
    Accept the following POST parameters: phone_model,
    problem_desc, status, user.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = MobileRequest.objects.all()
    serializer_class = MobileRequestSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('phone_model', 'problem_desc', 'status',)


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
