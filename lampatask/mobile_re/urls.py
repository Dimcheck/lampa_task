from mobile_re.views import MobileRequestUpdateDeleteView, MobileInvoiceUpdateDeleteView

from django.contrib import admin
from django.urls import include, path


app_name = 'mobile_re'

urlpatterns = [
    path('client_request/<int:pk>/', MobileRequestUpdateDeleteView.as_view(), name='request-action'),
    path('repairman_invoice/<int:pk>/', MobileInvoiceUpdateDeleteView.as_view(), name='invoice-action'),
]
