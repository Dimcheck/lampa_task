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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RepairmansView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Repairman.objects.all()
    serializer_class = RepairmanSerializer


class ClientsView(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientRegistrationView(RegisterView):
    serializer_class = ClientCustomRegistrationSerializer


class RepairmanRegistrationView(RegisterView):
    serializer_class = RepairmanCustomRegistrationSerializer
