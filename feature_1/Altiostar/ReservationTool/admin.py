from django.contrib import admin
from ReservationTool.models import *
from import_export.admin import ImportExportModelAdmin


# Creates TabularInline view for the Device model on required admin page
class DeviceInline(admin.TabularInline):
	model = Device

	def get_extra(self, request, obj=None, **kwargs):
		if obj:
			if obj.devices.exists():
				extra = 0
			else:
				extra = 1
		else:
			extra = 1
		return extra

# Creates TabularInline view for the Setup model on required admin page
class SetupInline(admin.TabularInline):
	model = Setup

	def get_extra(self, request, obj=None, **kwargs):
		if obj:
			if obj.setups.exists():
				extra = 0
			else:
				extra = 1
		else:
			extra = 1
		return extra


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
	inlines = [DeviceInline]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	inlines = [DeviceInline]


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
	inlines = [DeviceInline]


@admin.register(SetupType)
class SetupTypeAdmin(admin.ModelAdmin):
	inlines = [SetupInline]


@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
	inlines = [SetupInline]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	inlines = [SetupInline]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
	pass


# admin.site.register(Test)