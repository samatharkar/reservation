from django.shortcuts import render, HttpResponse
from ReservationTool.models import Device
from .models import *
import csv
from .filters import SetupFilter
from .filters import DeviceFilter


# Create your views here.
def home(request):
	return render(request, "home.html", {})


def add_setup(request):
    if request.method == "POST":
        setup_name = request.POST.get("setup_name")
        device_id = request.POST.get("device_type")
        attenuator_quantity = request.POST.get("attenuator_quantity")
        attenuator_db = request.POST.get("attenuator_db")
        device_type = Device.objects.get(id=device_id)
        Setup.objects.create(
            setup_name = setup_name,
            attenuator_quantity = attenuator_quantity, 
            attenuator_db = attenuator_db,
            device_type = device_type
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
        device_name = request.POST.get('device_name')
        device_srno = request.POST.get('device_srno')
        device_po_number = request.POST.get('device_po_number')
        device_po_date = request.POST.get('device_po_date')
        device_vendor = request.POST.get('device_vendor')
        device_invoice_number = request.POST.get('device_invoice_number')
        device_bonded = request.POST.get('device_bonded')
        device_bond_number = request.POST.get('device_bond_number')
        device_shipped_date = request.POST.get('device_shipped_date')
        device_arrival_date = request.POST.get('device_arrival_date')
        device_warranty_inmonths = request.POST.get('device_warranty_inmonths')
        device_added_byuser = request.POST.get('device_added_byuser')
        device_added_date = request.POST.get('device_added_date')
        device_description = request.POST.get('device_description')
        device_ownership = request.POST.get('device_ownership')
        
        Device.objects.create(
            device_name=device_name , 
            device_srno=device_srno , 
            device_po_number=device_po_number , 
            device_po_date=device_po_date , 
            device_vendor=device_vendor , 
            device_invoice_number=device_invoice_number,
            device_bonded=device_bonded,
            device_bond_number=device_bond_number,
            device_shipped_date=device_shipped_date,
            device_arrival_date=device_arrival_date,
            device_warranty_inmonths=device_warranty_inmonths,
            device_added_byuser=device_added_byuser,
            device_added_date=device_added_date,
            device_description=device_description,
            device_ownership=device_ownership

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

def add_device_type(request):
    if request.method == "POST":
        type_name = request.POST.get("type_name")
        type_make = request.POST.get("type_make")
        type_model = request.POST.get("type_model")
        type_part_no = request.POST.get("type_part_no")
        
        DeviceType.objects.create(
            type_name = type_name,
            type_make = type_make, 
            type_model = type_model,
            type_part_no = type_part_no
        )
        return render(
            request,
            "add_device_type.html",
            {
                'devices':Device.objects.all(),
                'msg':'Setup Added!'

            }
        )        
    else:
         return render(
             request,
             "add_device_type.html",
             {
                 'devices':Device.objects.all()
             }
           )


def add_vendor(request):
    if request.method == "POST":
        vendor_name = request.POST.get("vendor_name")
        vendor_email = request.POST.get("vendor_email")
        vendor_address = request.POST.get("vendor_address")
        vendor_number = request.POST.get("vendor_number")
        
        Vendor.objects.create(
            vendor_name = vendor_name,
            vendor_email = vendor_email, 
            vendor_address = vendor_address,
            vendor_number = vendor_number
        )
        return render(
            request,
            "add_vendor.html",
            {
                'devices':Device.objects.all(),
                'msg':'Setup Added!'

            }
        )        
    else:
         return render(
             request,
             "add_vendor.html",
             {
                 'devices':Device.objects.all()
             }
           )

def add_consumable(request):
    if request.method == "POST":
        consumable_name = request.POST.get("consumable_name")
        consumable_db = request.POST.get("consumable_db")
        consumable_connector1 = request.POST.get("consumable_connector1")
        consumable_connector2 = request.POST.get("consumable_connector2")
        consumable_watt = request.POST.get("consumable_watt")
        consumable_length = request.POST.get("consumable_length")
        consumable_quantity = request.POST.get("consumable_quantity")

        Consumable.objects.create(
            consumable_name = consumable_name,
            consumable_db = consumable_db, 
            consumable_connector1 = consumable_connector1,
            consumable_connector2 = consumable_connector2,
            consumable_watt = consumable_watt,
            consumable_length = consumable_length,
            consumable_quantity = consumable_quantity
        )
        return render(
            request,
            "add_consumables.html",
            {
                'devices':Device.objects.all(),
                'msg':'Setup Added!'

            }
        )        
    else:
         return render(
             request,
             "add_device_type.html",
             {
                 'devices':Device.objects.all()
             }
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
