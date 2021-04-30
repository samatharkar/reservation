from django.contrib import admin
from django.urls import path
from ReservationTool import views


urlpatterns = [
    path("", views.home, name='home'),
    path("add_device/", views.add_device, name='add_device'),
    # path("view_device/", views.view_device, name='view_device'),
    # path("add_setup/", views.add_setup, name='add_setup'),
    path("add_server_type/", views.add_server_type, name='add_server_type'),
    path("add_server/", views.add_server, name='add_server'),
    path("add_laptop/", views.add_laptop, name='add_laptop'),
    path("add_laptop_type/", views.add_laptop_type, name='add_laptop_type'),
    path("add_desktop/", views.add_desktop, name='add_desktop'),
    path("add_desktop_type/", views.add_desktop_type, name='add_desktop_type'),
    path("add_switch/", views.add_switch, name='add_switch'),
    path("add_switch_type/", views.add_switch_type, name='add_switch_type'),
    path("add_rrh/", views.add_rrh, name='add_rrh'),
    path("add_rrh_type/", views.add_rrh_type, name='add_rrh_type'),
    # path("view_setup/", views.view_setup, name='view_setup'),
    # path("search_setup/", views.search_setup, name='search_setup'),
    # path("search_device/", views.search_device, name='search_device'),
    # path("export/", views.export, name='export'),
]
