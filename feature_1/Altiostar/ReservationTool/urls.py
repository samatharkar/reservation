from django.contrib import admin
from django.urls import path
from ReservationTool import views


urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.userlogin, name='login'),
    path("logout/", views.userlogout, name='logout'),
    path("view-messages/", views.view_messages, name='view_messages'),
    path("dashboard/<str:name>/", views.dashboard, name='dashboard'),
    path("load-form/<str:name>/", views.load_object_form, name='load_object_form'),
    path("add-or-modify/<str:name>/", views.add_or_modify_object, name='add_or_modify_object'),
    path("view/<str:name>/", views.view_objects, name='view_objects'),
    path("search/<str:name>/", views.search_objects, name='search_objects'),
    path("delete/<str:name>/", views.delete_objects, name='delete_objects'),
    path("export/<str:name>/", views.export_objects, name='export_objects'),
    path("search-devices-for-setup/", views.search_devices_for_setup, name='search_devices_for_setup'),
    path("add-devices-to-setup/", views.add_devices_to_setup, name='add_devices_to_setup'),
    path("remove-devices-from-setup/", views.remove_devices_from_setup, name='remove_devices_from_setup'),
]
