from mobile_auth.views import ClientRegistrationView, RepairmanRegistrationView

from django.contrib import admin
from django.urls import include, path


app_name = 'mobile_auth'

urlpatterns = [
    path('registration/client/', ClientRegistrationView.as_view(), name='register-client'),
    path('registration/repairman/', RepairmanRegistrationView.as_view(), name='repairman-client'),
]
