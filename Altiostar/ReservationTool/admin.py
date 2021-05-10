from django.contrib import admin
from ReservationTool.models import *
<<<<<<< HEAD
=======
#from ReservationTool.models import Test
>>>>>>> main
from import_export.admin import ImportExportModelAdmin

# class DeviceAdmin(ImportExportModelAdmin):
#      pass

<<<<<<< HEAD
admin.site.register(Device, DeviceAdmin)
admin.site.register(CreateSetup)
admin.site.register(Vendor)
admin.site.register(Consumable)
admin.site.register(DeviceType)
admin.site.register(MakeSetup)
=======
# admin.site.register(Device, DeviceAdmin)
# admin.site.register(Setup)
admin.site.register(ServerType)
admin.site.register(Server)
# admin.site.register(DeviceType)
>>>>>>> main

# admin.site.register(Test)