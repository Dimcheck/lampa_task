from django.contrib import admin

from mobile_auth.models import Client, Repairman, CustomUser

admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(Repairman)
