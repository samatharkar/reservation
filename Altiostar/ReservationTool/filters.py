import django_filters
from .models import *

class SetupFilter(django_filters.FilterSet):
    setup_name = django_filters.CharFilter(lookup_expr='icontains') 

    class Meta:
        model = CreateSetup
        fields = ['setup_name' ]

class DeviceFilter(django_filters.FilterSet):
    hostname = django_filters.CharFilter(lookup_expr='icontains')  
    mac = django_filters.CharFilter(lookup_expr='icontains')  
    ip = django_filters.CharFilter(lookup_expr='icontains')  
    device_type = django_filters.CharFilter(lookup_expr='icontains')
    serial_number = django_filters.CharFilter(lookup_expr='icontains')  
    make = django_filters.CharFilter(lookup_expr='icontains')  

    class Meta:
        model = Device  
        fields = ['hostname']
