from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from mobile_auth.models import Client, CustomUser, Repairman
from mobile_auth.serializers import (ClientCustomRegistrationSerializer,
                                     ClientSerializer, CustomUserSerializer,
                                     RepairmanCustomRegistrationSerializer,
                                     RepairmanSerializer)


class CustomUsersView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RepairmansView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticated,)
    queryset = Repairman.objects.all()
    serializer_class = RepairmanSerializer


class ClientsView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientRegistrationView(RegisterView):
    """
    Accept the following POST parameters: username, password1, password2
    Return the REST Framework Token Object's key.

    In field "username" enter a phone number starting from 38 or 098,
    this field will go through a serializer and will have in the end result smth like:
    +380985673423.
    """
    queryset = CustomUser.objects.all()
    serializer_class = ClientCustomRegistrationSerializer


class RepairmanRegistrationView(RegisterView):
    """
    Accept the following POST parameters: username, password1, password2
    Return the REST Framework Token Object's key.
    """
    queryset = CustomUser.objects.all()
    serializer_class = RepairmanCustomRegistrationSerializer
