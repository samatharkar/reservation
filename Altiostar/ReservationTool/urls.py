from django.contrib import admin
from django.urls import path
from ReservationTool import views


urlpatterns = [
    path("", views.home, name='home'),
    path("add_device/", views.add_device, name='add_device'),
<<<<<<< HEAD
    path("view_device/", views.view_device, name='view_device'),
    path("add_setup/", views.add_setup, name='add_setup'),
    path("make_setup/", views.make_setup, name='make_setup'),
    path("add_device_type/", views.add_device_type, name='add_device_type'),
    path("add_consumable/", views.add_consumable, name='add_consumable'),
    path("add_vendor/", views.add_vendor, name='add_vendor'),
    path("view_setup/", views.view_setup, name='view_setup'),
    path("search_setup/", views.search_setup, name='search_setup'),
    path("search_device/", views.search_device, name='search_device'),
    path("export/", views.export, name='export'),
=======
    # path("view_device/", views.view_device, name='view_device'),
    # path("add_setup/", views.add_setup, name='add_setup'),
    path("add_server_type/", views.add_server_type, name='add_server_type'),
    path("add_server/", views.add_server, name='add_server'),
    # path("view_setup/", views.view_setup, name='view_setup'),
    # path("search_setup/", views.search_setup, name='search_setup'),
    # path("search_device/", views.search_device, name='search_device'),
    # path("export/", views.export, name='export'),
>>>>>>> main
]
