from django.contrib import admin
from django.urls import path
from ReservationTool import views


urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("add-device-type/", views.add_device_type, name='add_device_type'),
    path("add-vendor/", views.add_vendor, name='add_vendor'),
    path("add-consumable/", views.add_consumable, name='add_consumable'),
    path("add-team/", views.add_team, name='add_team'),
    path("add-device/", views.add_device, name='add_device'),
    path("view-device/", views.view_device, name='view_device'),
    path("search-device/", views.search_device, name='search_device'),
    path("add-setup-type/", views.add_setup_type, name='add_setup_type'),
    path("make-setup/", views.make_setup, name='make_setup'),
    path("add-devices-to-setup/", views.add_devices_to_setup, name='add_devices_to_setup_ajax'),
    path("view-setup/", views.view_setup, name='view_setup'),
    path("search-setup/", views.search_setup, name='search_setup'),
    path("export/", views.export, name='export'),
]
