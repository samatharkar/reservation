from django.contrib import admin
from ReservationTool.models import *
from import_export.admin import ImportExportModelAdmin

class DeviceAdmin(ImportExportModelAdmin):
     pass

admin.site.register(Device, DeviceAdmin)
admin.site.register(CreateSetup)
admin.site.register(Vendor)
admin.site.register(Consumable)
admin.site.register(DeviceType)
admin.site.register(MakeSetup)
admin.site.register(Team)
admin.site.register(SetupType)


# admin.site.register(Test)