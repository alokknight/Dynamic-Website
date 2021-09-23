from django.contrib import admin
from roomonrent.models import Tenant
from roomonrent.models import Owner,Room

# Register your models here.
admin.site.register(Tenant)
admin.site.register(Owner)
admin.site.register(Room)