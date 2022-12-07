from phonenumber_field.serializerfields import PhoneNumberField
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from mobile_auth.models import Client, Repairman, CustomUser


class RepairmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repairman
        fields = '__all__'


class ClientrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ClientCustomRegistrationSerializer(RegisterSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    username = PhoneNumberField(region='UA')

    def validate_username(self, username):
        return username.as_e164

    def save(self, request):
        user = super(ClientCustomRegistrationSerializer, self).save(request)
        user.is_client = True
        user.save()
        client = Client(client=user)
        client.save()
        return user


class RepairmanCustomRegistrationSerializer(RegisterSerializer):
    repairman = serializers.PrimaryKeyRelatedField(read_only=True)

    def save(self, request):
        user = super(RepairmanCustomRegistrationSerializer, self).save(request)
        user.is_repairman = True
        user.save()
        repairman = Repairman(repairman=user)
        repairman.save()
        return user

