from django.shortcuts import render, HttpResponse
from ReservationTool.models import Device
from .models import Device,Setup
import csv
from .filters import SetupFilter
from .filters import DeviceFilter


# Create your views here.
def home(request):
	return render(request, "home.html", {})


def add_setup(request):
    if request.method == "POST":
        setup_name = request.POST.get("setup_name")
        device_type = request.POST.get("device_type")
       # device = Device.objects.get(id=device_id)
        Setup.objects.create(
            setup_name=setup_name, 
            device = device
        )
        return render(
            request,
            "add_setup.html",
            {
                'devices':Device.objects.all(),
                'msg':'Setup Added!'

            }
        )        
    else:
         return render(
             request,
             "add_setup.html",
             {
                 'devices':Device.objects.all()
             }
           )

def add_device(request):
    if request.method == "POST":
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        serial_number = request.POST.get('serial_number')
        mac = request.POST.get('mac')
        device_type = request.POST.get('device')
        make = request.POST.get('make')
        Device.objects.create(
            hostname=hostname , 
            ip=ip , 
            serial_number=serial_number , 
            mac=mac , 
            device_type=device_type , 
            make=make
        )
        return render(
            request,
            "add_device.html",

        )
    else:
        return render(
            request,
            "add_device.html",

        )



# def add_device(request):
#     if request.method == "POST":
#         hostname = request.POST.get('hostname')
#         ip = request.POST.get('ip')
#         serial_number = request.POST.get('serial_number')
#         mac = request.POST.get('mac')
#         device_type = request.POST.get('device')
#         make = request.POST.get('make')
#         Device.objects.create(
#             hostname=hostname , ip=ip , serial_number=serial_number , mac=mac , device_type=device_type , make=make
#         )
#     else:
#         return render(
#             request,
#             "add_device.html",
#             {}
#         )

     
#         device = Device(hostname=hostname , ip=ip , serial_number=serial_number , mac=mac , device_type=device_type , make=make) 
#         device.save()
#     return render(request, "add_device.html", {})

def view_device(request):
    context = {}
    entries = Device.objects.all()
    context['entries'] = entries
    return render(request, 'view_device.html', context)

# def add_setup(request):

#         if request.method == "POST":
#             setup_name = request.POST.get("setup_name")
#             device_id = request.POST.get("device")
#             device = Device.objects.get(id=device_id)
#             Setup.objects.create(
#                 setup_name=setup_name,
#                 device = device
#             )
#         else:
#             return render(
#                 request,
#                 "add_setup.html",
#                 {
#                     'device':Device.objects.all()
#                 }
#             )
            #setup_name = request.POST.get('setup_name')
            # device_type = 
            #new_setup = request.POST.get(Device.objects.values('device_type'))
            #setup_name = Setup(setup_name=setup_name , new_setup=new_setup) 
            #setup_name.save()
        #return render(request, "add_setup.html",{}) 


def view_setup(request):
    context = {}
    setup_entries = Setup.objects.all()
    context['setup_entries'] = setup_entries
    return render(request, 'view_setup.html', context)

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fields.csv"'


    writer = csv.writer(response)
    writer.writerow(['Hostname', 'IP', 'MAC', 'Device Type', 'Serial Number', 'Make/Model'])

    for fields in Device.objects.all().values_list('hostname', 'ip', 'mac', 'device_type','serial_number', 'make'):
        writer.writerow(fields)

    return response

def search_setup(request):
    setup_list = Setup.objects.all()
    setup_filter = SetupFilter(request.GET, queryset=setup_list)
    return render(request, 'search_setup.html', {'filter': setup_filter })

def search_device(request):
     device_list = Device.objects.all()
     device_filter = DeviceFilter(request.GET, queryset=device_list)
     return render(request, 'search_device.html', {'filter': device_filter })
