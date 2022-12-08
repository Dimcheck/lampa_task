from django.contrib import admin

from mobile_re.models import MobileInvoice, MobileRequest

# Register your models here.
admin.site.register(MobileRequest)
admin.site.register(MobileInvoice)
