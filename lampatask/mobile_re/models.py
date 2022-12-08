from django.conf import settings
from django.db import models
from mobile_auth.models import Client


STATUS_CHOICES = (
    ('in queue', 'in queue'),
    ('in progress', 'in progress'),
    ('repaired', 'repaired'),
)


class MobileRequest(models.Model):
    user = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='request',
    )
    phone_model = models.CharField(max_length=50)
    problem_desc = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in progress')

    def __str__(self) -> str:
        return str([self.user, self.phone_model, self.status])


class MobileInvoice(models.Model):
    mobile_request = models.OneToOneField(
        MobileRequest,
        on_delete=models.CASCADE,
        blank=True,
        primary_key=True,
    )
    price = models.IntegerField()

    def __str__(self) -> str:
        return str([self.mobile_request, self.price + '$'])
