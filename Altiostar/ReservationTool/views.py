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
        name = request.POST.get("name")
        remark = request.POST.get("remark")
        # device_id = request.POST.get("device_type")
        # attenuator_quantity = request.POST.get("attenuator_quantity")
        # attenuator_db = request.POST.get("attenuator_db")
        # device_type = Device.objects.get(id=device_id)
        CreateSetup.objects.create(
            name = name,
            remark = remark
            # attenuator_quantity = attenuator_quantity, 
            # attenuator_db = attenuator_db,
            # device_type = device_type
        )
        return render(
            request,
            "add_setup.html",
            {
               # 'devices':Device.objects.all(),
                'msg':'Setup Added!'

            }
        )        
    else:
         return render(
             request,
             "add_setup.html"
            # , {
            #      'devices':Device .objects.all()
            #  }
           )

def add_device(request):
    if request.method == "POST":
        name = request.POST.get('name')
        type_id = request.POST.get('type')
        type = DeviceType.objects.get(id=type_id)
        #consumable = request.POST.get('device_consumable')
        srno = request.POST.get('srno')
        po_number = request.POST.get('po_number')
        po_date = request.POST.get('po_date')
        vendor_id = request.POST.get('vendor')
        vendor = Vendor.objects.get(id=vendor_id)
        invoice_number = request.POST.get('invoice_number')
        bonded = request.POST.get('bonded')
        bond_number = request.POST.get('bond_number')
        shipped_date = request.POST.get('shipped_date')
        arrival_date = request.POST.get('arrival_date')
        warranty_inmonths = request.POST.get('warranty_inmonths')
        added_byuser = request.POST.get('added_byuser')
        added_date = request.POST.get('added_date')
        ownership = request.POST.get('ownership')
        remark = request.POST.get('remark')
        
        Device.objects.create(
            name = name , 
            type = type ,
         #   device_consumable = device_consumable,
            srno=srno , 
            po_number=po_number , 
            po_date=po_date , 
            vendor=vendor , 
            invoice_number=invoice_number,
            bonded=bonded,
            bond_number=bond_number,
            shipped_date=shipped_date,
            arrival_date=arrival_date,
            warranty_inmonths=warranty_inmonths,
            added_byuser=added_byuser,
            added_date=added_date,
            ownership=ownership,
            remark=remark

        )
        return render(
            request,
            "add_device.html",
            {
                'vendors':Vendor.objects.all(),
                'd_type':DeviceType.objects.all(),
                'msg':'Device Added!'

          #      'con':Consumable.objects.all(),

            }
        )  
        
    else:
        return render(
            request,
            "add_device.html",

            {
                'vendors':Vendor.objects.all(),
                'd_type':DeviceType.objects.all(),
           #     'con':Consumable.objects.all(),

            }
        
        )

def add_device_type(request):
    if request.method == "POST":
        name = request.POST.get("name")
        make = request.POST.get("make")
        model = request.POST.get("model")
        part_no = request.POST.get("part_no")
        remark = request.POST.get("remark")

        DeviceType.objects.create(
            name = name,
            make = make, 
            model = model,
            part_no = part_no,
            remark = remark
        )
        return render(
            request,
            "add_device_type.html",
            {
            'msg':'Device Type Added!'

            }

        )        
    else:
         return render(
             request,
             "add_device_type.html",

           )


def add_vendor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        number = request.POST.get("number")
        remark = request.POST.get("remark")
        
        Vendor.objects.create(
            name = name,
            email = email, 
            address = address,
            number = number,
            remark = remark
        )
        return render(
            request,
            "add_vendor.html",
            {
             'msg':'Vendor Added!'

            }
            

        )        
    else:
         return render(
             request,
             "add_vendor.html",

           )

def add_consumable(request):
    if request.method == "POST":
        name = request.POST.get("name")
        db = request.POST.get("db")
        connector1 = request.POST.get("connector1")
        connector2 = request.POST.get("connector2")
        watt = request.POST.get("watt")
        length = request.POST.get("length")
        quantity = request.POST.get("quantity")
        remark = request.POST.get("remark")
        

        Consumable.objects.create(
            name = name,
            db = db, 
            connector1 = connector1,
            connector2 = connector2,
            watt = watt,
            length = length,
            quantity = quantity,
            remark = remark
        )
        return render(
            request,
            "add_consumable.html",
            {
            'msg':'Consumable Added!'

            }
        )        
    else:
         return render(
             request,
             "add_consumable.html",

           )

def make_setup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        device_id = request.POST.get("device")
        device = Device.objects.get(id=device_id)
        consumable_id = request.POST.get("consumable")
        consumable = Consumable.objects.get(id=consumable_id)
        type_id = request.POST.get("type")
        type = DeviceType.objects.get(id=type_id)

        MakeSetup.objects.create(
            name = name,
            device = device,
            consumable = consumable,
            type = type

        )
        return render(
            request,
            "make_setup.html",
            {
                'device_n':Device.objects.all(),
                #'setup_n':CreateSetup.objects.all(),
                'consumable_n':Consumable.objects.all(),
                'msg':'Setup Added!'

            }
        )        
    else:
         return render(
             request,
             "make_setup.html",
             {
                'device_n':Device.objects.all(),
               # 'setup_n':CreateSetup.objects.all(),
                'consumable_n':Consumable.objects.all(),
                'type_n':DeviceType.objects.all(),
             #   'msg':'Setup Added!'

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
    setup_entries = CreateSetup.objects.all()
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
    setup_list = CreateSetup.objects.all()
    setup_filter = SetupFilter(request.GET, queryset=setup_list)
    return render(request, 'search_setup.html', {'filter': setup_filter })

def search_device(request):
     device_list = Device.objects.all()
     device_filter = DeviceFilter(request.GET, queryset=device_list)
     return render(request, 'search_device.html', {'filter': device_filter })

def login(request):
    pass
    return render(request, 'login.html')