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
    login = PhoneNumberField(region='UA')

    def get_cleaned_data(self):
        data = super(ClientCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'login': self.validated_data.get('login', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(ClientCustomRegistrationSerializer, self).save(request)
        user.is_client = True
        user.save()
        client = Client(client=user, login=self.cleaned_data.get('login'))
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

