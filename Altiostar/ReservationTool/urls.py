from django.contrib import admin
from django.urls import path
from ReservationTool import views


urlpatterns = [
    path("", views.home, name='home'),
    path("add_device/", views.add_device, name='add_device'),
    path("view_device/", views.view_device, name='view_device'),
    path("add_setup/", views.add_setup, name='add_setup'),
    path("view_setup/", views.view_setup, name='view_setup'),
    path("search_setup/", views.search_setup, name='search_setup'),
    path("search_device/", views.search_device, name='search_device'),
    path("export/", views.export, name='export'),
]
