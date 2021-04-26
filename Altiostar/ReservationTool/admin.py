from django.contrib import admin
from ReservationTool.models import Device, Setup
#from ReservationTool.models import Test
from import_export.admin import ImportExportModelAdmin

class DeviceAdmin(ImportExportModelAdmin):
     pass

admin.site.register(Device, DeviceAdmin)
admin.site.register(Setup)
# admin.site.register(SetupType)
# admin.site.register(DeviceType)

# admin.site.register(Test)