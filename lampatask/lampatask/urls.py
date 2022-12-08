"""lampatask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from mobile_auth.views import (ClientRegistrationView, ClientsView,
                               CustomUsersView, RepairmanRegistrationView,
                               RepairmansView)

from mobile_re.views import MobileRequestView, MobileInvoiceView
from rest_framework.routers import DefaultRouter
# import allauth

router = DefaultRouter()
router.register(r'clients', ClientsView, basename='client_view')
router.register(r'repairmans', RepairmansView, basename='repairman_view')
router.register(r'users', CustomUsersView, basename='users_view')
router.register(r'user_request', MobileRequestView, basename='requests_view')
router.register(r'repairman_invoice', MobileInvoiceView, basename='invoices_view')

app_name = 'mobile_auth'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('registration/client/', ClientRegistrationView.as_view(), name='register-client'),
    path('registration/repairman/', RepairmanRegistrationView.as_view(), name='repairman-client'),
    path('accounts/', include('allauth.urls')),

] + router.urls
