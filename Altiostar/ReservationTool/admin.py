from django.contrib import admin
from ReservationTool.models import *
#from ReservationTool.models import Test
from import_export.admin import ImportExportModelAdmin

# class DeviceAdmin(ImportExportModelAdmin):
#      pass

# admin.site.register(Device, DeviceAdmin)
# admin.site.register(Setup)
admin.site.register(ServerType)
admin.site.register(Server)
# admin.site.register(DeviceType)

# admin.site.register(Test)