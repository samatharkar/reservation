from django.contrib import admin
from ReservationTool.models import *
from import_export.admin import ImportExportModelAdmin


class DeviceAdmin(ImportExportModelAdmin):
     pass


class DeviceInline(admin.TabularInline):
	model = Device


class SetupAdmin(admin.ModelAdmin):
	inlines = [DeviceInline]


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType)
admin.site.register(Vendor)
admin.site.register(Consumable)
admin.site.register(SetupType)
admin.site.register(Setup, SetupAdmin)
admin.site.register(Team)


# admin.site.register(Test)