from django.contrib import admin
from django.urls import path
from ReservationTool import views


urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("view_messages/", views.view_messages, name='view_messages'),
    path("dashboard/<str:name>/", views.dashboard, name='dashboard'),
    path("load_object_form/<str:name>/", views.load_object_form, name='load_object_form'),
    path("add_or_modify_object/<str:name>/", views.add_or_modify_object, name='add_or_modify_object'),
    path("view_objects/<str:name>/", views.view_objects, name='view_objects'),
    path("search_objects/<str:name>/", views.search_objects, name='search_objects'),
    path("delete_objects/<str:name>/", views.delete_objects, name='delete_objects'),
    path("search_devices_for_setup/", views.search_devices_for_setup, name='search_devices_for_setup'),
    path("add_devices_to_setup/", views.add_devices_to_setup, name='add_devices_to_setup'),
    path("export/", views.export, name='export'),
]
