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
admin.site.register(RrhType)
admin.site.register(RRH)
admin.site.register(SwitchType)
admin.site.register(Switch)
admin.site.register(DesktopType)
admin.site.register(Desktop)
admin.site.register(LaptopType)
admin.site.register(Laptop)
# admin.site.register(Test)