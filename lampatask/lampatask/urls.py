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
from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import include, path, re_path
from mobile_auth.views import ClientsView, CustomUsersView, RepairmansView
from mobile_re.views import MobileInvoiceView, MobileRequestView
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'clients', ClientsView, basename='client_view')
router.register(r'repairmans', RepairmansView, basename='repairman_view')
router.register(r'users', CustomUsersView, basename='users_view')
router.register(r'client/request/', MobileRequestView, basename='requests_view')
router.register(r'repairman/invoice/', MobileInvoiceView, basename='invoices_view')


urlpatterns = [
    path('', include('mobile_re.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users-auth/', include('mobile_auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + router.urls
