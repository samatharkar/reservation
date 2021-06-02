from django.contrib import admin
from django.urls import path
from ReservationTool import views


urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("adddevice_type/", views.add_device_type, name='add_device_type'),
    path("add_vendor/", views.add_vendor, name='add_vendor'),
    path("add_consumable/", views.add_consumable, name='add_consumable'),
    path("add_team/", views.add_team, name='add_team'),
    path("add_device/", views.add_device, name='add_device'),
    path("view_device/", views.view_device, name='view_device'),
    path("search_device/", views.search_device, name='search_device'),
    path("add_setup_type/", views.add_setup_type, name='add_setup_type'),
    path("make_setup/", views.make_setup, name='make_setup'),
    path("search_devices_for_setup/", views.search_devices_for_setup, name='search_devices_for_setup_ajax'),
    path("add_devices_to_setup/", views.add_devices_to_setup, name='add_devices_to_setup_ajax'),
    path("view_setup/", views.view_setup, name='view_setup'),
    path("search_setup/", views.search_setup, name='search_setup'),
    path("export/", views.export, name='export'),
]
