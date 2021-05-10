from django.shortcuts import render, HttpResponse
<<<<<<< HEAD
from ReservationTool.models import Device
from .models import *
=======
# from ReservationTool.models import Device
from .models import ServerType, Server
>>>>>>> main
import csv
# from .filters import SetupFilter
# from .filters import DeviceFilter


# Create your views here.
def home(request):
	return render(request, "home.html", {})


<<<<<<< HEAD
def add_setup(request):
    if request.method == "POST":
        create_setup_name = request.POST.get("create_setup_name")
        create_setup_remark = request.POST.get("create_setup_remark")
        # device_id = request.POST.get("device_type")
        # attenuator_quantity = request.POST.get("attenuator_quantity")
        # attenuator_db = request.POST.get("attenuator_db")
        # device_type = Device.objects.get(id=device_id)
        CreateSetup.objects.create(
            create_setup_name = create_setup_name,
            create_setup_remark = create_setup_remark
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
        device_name = request.POST.get('device_name')
        device_type = request.POST.get('device_type')
        #device_consumable = request.POST.get('device_consumable')
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
        device_ownership = request.POST.get('device_ownership')
        device_remark = request.POST.get('device_remark')
        
        Device.objects.create(
            device_name = device_name , 
            device_type = device_type ,
         #   device_consumable = device_consumable,
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
            device_ownership=device_ownership,
            device_remark=device_remark

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
=======
# def add_setup(request):
#     if request.method == "POST":
#         setup_name = request.POST.get("setup_name")
#         device_id = request.POST.get("device_type")
#         attenuator_quantity = request.POST.get("attenuator_quantity")
#         attenuator_db = request.POST.get("attenuator_db")
#         device_type = Device.objects.get(id=device_id)
#         Setup.objects.create(
#             setup_name = setup_name,
#             attenuator_quantity = attenuator_quantity, 
#             attenuator_db = attenuator_db,
#             device_type = device_type
#         )
#         return render(
#             request,
#             "add_setup.html",
#             {
#                 'devices':Device.objects.all(),
#                 'msg':'Setup Added!'

#             }
#         )        
#     else:
#          return render(
#              request,
#              "add_setup.html",
#              {
#                  'devices':Device.objects.all()
#              }
#            )

# def add_device_old(request):
#     if request.method == "POST":
#         hostname = request.POST.get('hostname')
#         ip = request.POST.get('ip')
#         serial_number = request.POST.get('serial_number')
#         mac = request.POST.get('mac')
#         device_type = request.POST.get('device')
#         make = request.POST.get('make')
#         Device.objects.create(
#             hostname=hostname , 
#             ip=ip , 
#             serial_number=serial_number , 
#             mac=mac , 
#             device_type=device_type , 
#             make=make
#         )
#         return render(
#             request,
#             "add_device_old.html",

#         )
#     else:
#         return render(
#             request,
#             "add_device_old.html",

#         )
>>>>>>> main

def add_device_type(request):
    if request.method == "POST":
        type_name = request.POST.get("type_name")
        type_make = request.POST.get("type_make")
        type_model = request.POST.get("type_model")
        type_part_no = request.POST.get("type_part_no")
        type_remark = request.POST.get("type_remark")

        DeviceType.objects.create(
            type_name = type_name,
            type_make = type_make, 
            type_model = type_model,
            type_part_no = type_part_no,
            type_remark = type_remark
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
        vendor_name = request.POST.get("vendor_name")
        vendor_email = request.POST.get("vendor_email")
        vendor_address = request.POST.get("vendor_address")
        vendor_number = request.POST.get("vendor_number")
        vendor_remark = request.POST.get("vendor_remark")
        
        Vendor.objects.create(
            vendor_name = vendor_name,
            vendor_email = vendor_email, 
            vendor_address = vendor_address,
            vendor_number = vendor_number,
            vendor_remark = vendor_remark
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
        consumable_name = request.POST.get("consumable_name")
        consumable_db = request.POST.get("consumable_db")
        consumable_connector1 = request.POST.get("consumable_connector1")
        consumable_connector2 = request.POST.get("consumable_connector2")
        consumable_watt = request.POST.get("consumable_watt")
        consumable_length = request.POST.get("consumable_length")
        consumable_quantity = request.POST.get("consumable_quantity")
        consumable_remark = request.POST.get("consumable_remark")
        

        Consumable.objects.create(
            consumable_name = consumable_name,
            consumable_db = consumable_db, 
            consumable_connector1 = consumable_connector1,
            consumable_connector2 = consumable_connector2,
            consumable_watt = consumable_watt,
            consumable_length = consumable_length,
            consumable_quantity = consumable_quantity,
            consumable_remark = consumable_remark
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
        make_setup_name = request.POST.get("make_setup_name")
        make_setup_device = request.POST.get("make_setup_device")
        make_setup_consumable = request.POST.get("make_setup_consumable")

        MakeSetup.objects.create(
            make_setup_name = make_setup_name,
            make_setup_device = make_setup_device,
            make_setup_consumable = make_setup_consumable

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

# def view_device(request):
#     context = {}
#     entries = Device.objects.all()
#     context['entries'] = entries
#     return render(request, 'view_device.html', context)

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


<<<<<<< HEAD
def view_setup(request):
    context = {}
    setup_entries = CreateSetup.objects.all()
    context['setup_entries'] = setup_entries
    return render(request, 'view_setup.html', context)
=======
# def view_setup(request):
#     context = {}
#     setup_entries = Setup.objects.all()
#     context['setup_entries'] = setup_entries
#     return render(request, 'view_setup.html', context)

# def export(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="fields.csv"'


#     writer = csv.writer(response)
#     writer.writerow(['Hostname', 'IP', 'MAC', 'Device Type', 'Serial Number', 'Make/Model'])

#     for fields in Device.objects.all().values_list('hostname', 'ip', 'mac', 'device_type','serial_number', 'make'):
#         writer.writerow(fields)
>>>>>>> main

#     return response

# def search_setup(request):
#     setup_list = Setup.objects.all()
#     setup_filter = SetupFilter(request.GET, queryset=setup_list)
#     return render(request, 'search_setup.html', {'filter': setup_filter })

# def search_device(request):
#      device_list = Device.objects.all()
#      device_filter = DeviceFilter(request.GET, queryset=device_list)
#      return render(request, 'search_device.html', {'filter': device_filter })


def add_server_type(request):
    if request.method == "POST":
        server_type_name = request.POST.get('server_type_name')
        server_make = request.POST.get('server_make')
        server_model = request.POST.get('server_model')
        server_processor = request.POST.get('server_processor')
        server_socket = request.POST.get('server_socket')
        server_core = request.POST.get('server_core')
        server_hdd_model = request.POST.get('server_hdd_model')
        server_hdd_size = request.POST.get('server_hdd_size')
        server_hdd_number = request.POST.get('server_hdd_number')
        server_ram = request.POST.get('server_ram')

        ServerType.objects.create(
            server_type_name=server_type_name , 
            server_make=server_make , 
            server_model=server_model , 
            server_processor=server_processor , 
            server_socket=server_socket , 
            server_core=server_core,
            server_hdd_model=server_hdd_model , 
            server_hdd_size=server_hdd_size , 
            server_hdd_number=server_hdd_number , 
            server_ram=server_ram
        )
        return render(
            request,
            "add_server_type.html",

<<<<<<< HEAD
def search_setup(request):
    setup_list = CreateSetup.objects.all()
    setup_filter = SetupFilter(request.GET, queryset=setup_list)
    return render(request, 'search_setup.html', {'filter': setup_filter })
=======
        )
    else:
        return render(
            request,
            "add_server_type.html",
>>>>>>> main

        )

    # if request.method.POST
    # return render(request, 'add_server_type.html')
 

def add_device(request):
    return render(request, 'add_device.html')

def add_server(request):
    if request.method == "POST":
        server_id = request.POST.get("server_type_name")
        server_type_name = ServerType.objects.get(id=server_id)
       # server_model = request.POST.get("server_model")
        server_name = request.POST.get("server_name")
        server_serial_number = request.POST.get("server_serial_number")
        server_po_number = request.POST.get("server_po_number")
        server_po_date = request.POST.get("server_po_date")
        server_vendor = request.POST.get("server_vendor")
        server_invoice = request.POST.get("server_invoice")
        server_bond = request.POST.get("server_bond")
        server_bond_number = request.POST.get("server_bond_number")
        server_type = request.POST.get("server_type")
        server_ship_date = request.POST.get("server_ship_date")
        server_arrival_date = request.POST.get("server_arrival_date")
        server_warranty = request.POST.get("server_warranty")
        server_added_byuser = request.POST.get("server_added_byuser")
        server_added_ondate = request.POST.get("server_added_ondate")
        server_ownership = request.POST.get("server_ownership")
        server_ip_address = request.POST.get("server_ip_address")
        server_hostname = request.POST.get("server_hostname")
        server_mgmt_mac = request.POST.get("server_mgmt_mac")
        server_lan_mac = request.POST.get("server_lan_mac")
        server_os = request.POST.get("server_os")
        server_fversion = request.POST.get("server_fversion")
        server_hardware_revision = request.POST.get("server_hardware_revision")
        server_setup_id = request.POST.get("server_setup_id")
        server_remark = request.POST.get("server_remark")
        server_type_name = ServerType.objects.get(id=server_id)
        Server.objects.create(
            server_type_name = server_type_name,
            server_name = server_name,
         #   server_model = server_model, 
            server_serial_number = server_serial_number,
            server_po_number = server_po_number,
            server_po_date = server_po_date,
            server_vendor = server_vendor, 
            server_invoice = server_invoice,
            server_bond = server_bond,
            server_bond_number = server_bond_number,
            server_type = server_type, 
            server_ship_date = server_ship_date,
            server_arrival_date = server_arrival_date,
            server_warranty = server_warranty,
            server_added_byuser = server_added_byuser,
            server_added_ondate = server_added_ondate,
            server_ownership = server_ownership,
            server_ip_address = server_ip_address,
            server_hostname = server_hostname,
            server_mgmt_mac = server_mgmt_mac ,
            server_lan_mac = server_lan_mac ,
            server_os = server_os,
            server_fversion = server_fversion,
            server_hardware_revision = server_hardware_revision,
            server_setup_id = server_setup_id,
            server_remark = server_remark,

        )
        return render(
            request,
            "add_server.html",
            {
                'server_tn':ServerType.objects.all(),
                'msg':'Server Added!'

            }
        )        
    else:
         return render(
             request,
             "add_server.html",
             {
                 'server_tn':ServerType.objects.all()
             }
           )
    
    return render(request, 'add_server.html')