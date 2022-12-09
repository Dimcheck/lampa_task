from mobile_re.views import MobileRequestUpdateDeleteView

from django.contrib import admin
from django.urls import include, path


app_name = 'mobile_re'

urlpatterns = [
    path('client/request_update/<int:pk>/', MobileRequestUpdateDeleteView.as_view(), name='register-client'),
]
