from django.contrib import admin
from ReservationTool.models import *
from import_export.admin import ImportExportModelAdmin


class DeviceAdmin(ImportExportModelAdmin):
     pass


class SetupAdmin(admin.ModelAdmin):
	list_display = ('name', 'added_devices')

	def added_devices(self, setup):
		return ", ".join([
			device.name for device in setup.devices.all()
		])

	added_devices.short_description = "Added Devices"


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType)
admin.site.register(Vendor)
admin.site.register(Consumable)
admin.site.register(SetupType)
admin.site.register(Setup, SetupAdmin)
admin.site.register(Team)


# admin.site.register(Test)