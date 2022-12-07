from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_repairman = models.BooleanField(default=False)


class Client(models.Model):
    client = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        # primary_key=True,
    )
    login = PhoneNumberField(region='UA')

    def __repr__(self) -> str:
        return str([self.client.login, self.client.password])


class Repairman(models.Model):
    repairman = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        # primary_key=True,
    )

    def __repr__(self) -> str:
        return str([self.repairman.username, self.repairman.password])
