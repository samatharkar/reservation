from django.shortcuts import render, HttpResponse
# from ReservationTool.models import Device
from .models import *
import csv
# from .filters import SetupFilter
# from .filters import DeviceFilter


# Create your views here.
def home(request):
	return render(request, "home.html", {})


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

        )
    else:
        return render(
            request,
            "add_server_type.html",

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




def add_rrh_type(request):
    if request.method == "POST":
        rrh_type_name = request.POST.get('rrh_type_name')
        rrh_part_number = request.POST.get('rrh_part_number')
        rrh_model_number = request.POST.get('rrh_model_number')
        rrh_band = request.POST.get('rrh_band')
        rrh_remark = request.POST.get('rrh_remark')

        RrhType.objects.create(
            rrh_type_name=rrh_type_name , 
            rrh_part_number=rrh_part_number , 
            rrh_model_number=rrh_model_number , 
            rrh_band=rrh_band , 
            rrh_remark=rrh_remark 
        )
        return render(
            request,
            "add_rrh_type.html",

        )
    else:
        return render(
            request,
            "add_rrh_type.html",

        )

def add_rrh(request):
    if request.method == "POST":
        rrh_id = request.POST.get("rrh_type_name")
        rrh_type_name = RrhType.objects.get(id=rrh_id)
       # rrh_model = request.POST.get("rrh_model")
        rrh_name = request.POST.get("rrh_name")
        rrh_serial_number = request.POST.get("rrh_serial_number")
        rrh_po_number = request.POST.get("rrh_po_number")
        rrh_po_date = request.POST.get("rrh_po_date")
        rrh_vendor = request.POST.get("rrh_vendor")
        rrh_invoice = request.POST.get("rrh_invoice")
        rrh_bond = request.POST.get("rrh_bond")
        rrh_bond_number = request.POST.get("rrh_bond_number")
        rrh_type = request.POST.get("rrh_type")
        rrh_ship_date = request.POST.get("rrh_ship_date")
        rrh_arrival_date = request.POST.get("rrh_arrival_date")
        rrh_warranty = request.POST.get("rrh_warranty")
        rrh_added_byuser = request.POST.get("rrh_added_byuser")
        rrh_added_ondate = request.POST.get("rrh_added_ondate")
        rrh_ownership = request.POST.get("rrh_ownership")
        rrh_ip_address = request.POST.get("rrh_ip_address")
        rrh_hostname = request.POST.get("rrh_hostname")
        rrh_mgmt_mac = request.POST.get("rrh_mgmt_mac")
        rrh_lan_mac = request.POST.get("rrh_lan_mac")
        rrh_os = request.POST.get("rrh_os")
        rrh_fversion = request.POST.get("rrh_fversion")
        rrh_hardware_revision = request.POST.get("rrh_hardware_revision")
        rrh_setup_id = request.POST.get("rrh_setup_id")
        rrh_remark = request.POST.get("rrh_remark")
        rrh_type_name = RrhType.objects.get(id=rrh_id)
        RRH.objects.create(
            rrh_type_name = rrh_type_name,
            rrh_name = rrh_name,
         #   rrh_model = rrh_model, 
            rrh_serial_number = rrh_serial_number,
            rrh_po_number = rrh_po_number,
            rrh_po_date = rrh_po_date,
            rrh_vendor = rrh_vendor, 
            rrh_invoice = rrh_invoice,
            rrh_bond = rrh_bond,
            rrh_bond_number = rrh_bond_number,
            rrh_type = rrh_type, 
            rrh_ship_date = rrh_ship_date,
            rrh_arrival_date = rrh_arrival_date,
            rrh_warranty = rrh_warranty,
            rrh_added_byuser = rrh_added_byuser,
            rrh_added_ondate = rrh_added_ondate,
            rrh_ownership = rrh_ownership,
            rrh_ip_address = rrh_ip_address,
            rrh_hostname = rrh_hostname,
            rrh_mgmt_mac = rrh_mgmt_mac ,
            rrh_lan_mac = rrh_lan_mac ,
            rrh_os = rrh_os,
            rrh_fversion = rrh_fversion,
            rrh_hardware_revision = rrh_hardware_revision,
            rrh_setup_id = rrh_setup_id,
            rrh_remark = rrh_remark,

        )
        return render(
            request,
            "add_rrh.html",
            {
                'rrh_tn':RrhType.objects.all(),
                'msg':'rrh Added!'

            }
        )        
    else:
         return render(
             request,
             "add_rrh.html",
             {
                 'rrh_tn':RrhType.objects.all()
             }
           )
    
    return render(request, 'add_rrh.html')




def add_desktop_type(request):
    if request.method == "POST":
        desktop_type_name = request.POST.get('desktop_type_name')
        desktop_make = request.POST.get('desktop_make')
        desktop_model = request.POST.get('desktop_model')
        desktop_processor = request.POST.get('desktop_processor')
        desktop_ram = request.POST.get('desktop_ram')
        desktop_hdd_model = request.POST.get('desktop_hdd_model')
        desktop_hdd_size = request.POST.get('desktop_hdd_size')
        desktop_display_size = request.POST.get('desktop_display_size')

        DesktopType.objects.create(
            desktop_type_name=desktop_type_name , 
            desktop_make=desktop_make , 
            desktop_model=desktop_model , 
            desktop_processor=desktop_processor , 
            desktop_ram = desktop_ram,
            desktop_hdd_model = desktop_hdd_model , 
            desktop_hdd_size = desktop_hdd_size, 
            desktop_display_size=desktop_display_size, 

        )
        return render(
            request,
            "add_desktop_type.html",

        )
    else:
        return render(
            request,
            "add_desktop_type.html",

        )

def add_desktop(request):
    if request.method == "POST":
        desktop_id = request.POST.get("desktop_type_name")
        desktop_type_name = DesktopType.objects.get(id=desktop_id)
       # desktop_model = request.POST.get("desktop_model")
        desktop_name = request.POST.get("desktop_name")
        desktop_serial_number = request.POST.get("desktop_serial_number")
        desktop_po_number = request.POST.get("desktop_po_number")
        desktop_po_date = request.POST.get("desktop_po_date")
        desktop_vendor = request.POST.get("desktop_vendor")
        desktop_invoice = request.POST.get("desktop_invoice")
        desktop_bond = request.POST.get("desktop_bond")
        desktop_bond_number = request.POST.get("desktop_bond_number")
        desktop_type = request.POST.get("desktop_type")
        desktop_ship_date = request.POST.get("desktop_ship_date")
        desktop_arrival_date = request.POST.get("desktop_arrival_date")
        desktop_warranty = request.POST.get("desktop_warranty")
        desktop_added_byuser = request.POST.get("desktop_added_byuser")
        desktop_added_ondate = request.POST.get("desktop_added_ondate")
        desktop_ownership = request.POST.get("desktop_ownership")
        desktop_ip_address = request.POST.get("desktop_ip_address")
        desktop_hostname = request.POST.get("desktop_hostname")
        desktop_mgmt_mac = request.POST.get("desktop_mgmt_mac")
        desktop_lan_mac = request.POST.get("desktop_lan_mac")
        desktop_os = request.POST.get("desktop_os")
        desktop_fversion = request.POST.get("desktop_fversion")
        desktop_hardware_revision = request.POST.get("desktop_hardware_revision")
        desktop_setup_id = request.POST.get("desktop_setup_id")
        desktop_remark = request.POST.get("desktop_remark")
        desktop_type_name = DesktopType.objects.get(id=desktop_id)
        Desktop.objects.create(
            desktop_type_name = desktop_type_name,
            desktop_name = desktop_name,
         #   desktop_model = desktop_model, 
            desktop_serial_number = desktop_serial_number,
            desktop_po_number = desktop_po_number,
            desktop_po_date = desktop_po_date,
            desktop_vendor = desktop_vendor, 
            desktop_invoice = desktop_invoice,
            desktop_bond = desktop_bond,
            desktop_bond_number = desktop_bond_number,
            desktop_type = desktop_type, 
            desktop_ship_date = desktop_ship_date,
            desktop_arrival_date = desktop_arrival_date,
            desktop_warranty = desktop_warranty,
            desktop_added_byuser = desktop_added_byuser,
            desktop_added_ondate = desktop_added_ondate,
            desktop_ownership = desktop_ownership,
            desktop_ip_address = desktop_ip_address,
            desktop_hostname = desktop_hostname,
            desktop_mgmt_mac = desktop_mgmt_mac ,
            desktop_lan_mac = desktop_lan_mac ,
            desktop_os = desktop_os,
            desktop_fversion = desktop_fversion,
            desktop_hardware_revision = desktop_hardware_revision,
            desktop_setup_id = desktop_setup_id,
            desktop_remark = desktop_remark,

        )
        return render(
            request,
            "add_desktop.html",
            {
                'desktop_tn':DesktopType.objects.all(),
                'msg':'desktop Added!'

            }
        )        
    else:
         return render(
             request,
             "add_desktop.html",
             {
                 'desktop_tn':DesktopType.objects.all()
             }
           )
    
    return render(request, 'add_desktop.html')




def add_switch_type(request):
    if request.method == "POST":
        switch_type_name = request.POST.get('switch_type_name')
        switch_part_number = request.POST.get('switch_part_number')
        switch_model_number = request.POST.get('switch_model_number')
        switch_remark = request.POST.get('switch_remark')

        SwitchType.objects.create(
            switch_type_name=switch_type_name , 
            switch_part_number=switch_part_number , 
            switch_model_number=switch_model_number , 
            switch_remark=switch_remark 
        )
        return render(
            request,
            "add_switch_type.html",

        )
    else:
        return render(
            request,
            "add_switch_type.html",

        )

def add_switch(request):
    if request.method == "POST":
        switch_id = request.POST.get("switch_type_name")
        switch_type_name = SwitchType.objects.get(id=switch_id)
       # switch_model = request.POST.get("switch_model")
        switch_name = request.POST.get("switch_name")
        switch_serial_number = request.POST.get("switch_serial_number")
        switch_po_number = request.POST.get("switch_po_number")
        switch_po_date = request.POST.get("switch_po_date")
        switch_vendor = request.POST.get("switch_vendor")
        switch_invoice = request.POST.get("switch_invoice")
        switch_bond = request.POST.get("switch_bond")
        switch_bond_number = request.POST.get("switch_bond_number")
        switch_type = request.POST.get("switch_type")
        switch_ship_date = request.POST.get("switch_ship_date")
        switch_arrival_date = request.POST.get("switch_arrival_date")
        switch_warranty = request.POST.get("switch_warranty")
        switch_added_byuser = request.POST.get("switch_added_byuser")
        switch_added_ondate = request.POST.get("switch_added_ondate")
        switch_ownership = request.POST.get("switch_ownership")
        switch_ip_address = request.POST.get("switch_ip_address")
        switch_hostname = request.POST.get("switch_hostname")
        switch_mgmt_mac = request.POST.get("switch_mgmt_mac")
        switch_lan_mac = request.POST.get("switch_lan_mac")
        switch_os = request.POST.get("switch_os")
        switch_fversion = request.POST.get("switch_fversion")
        switch_hardware_revision = request.POST.get("switch_hardware_revision")
        switch_setup_id = request.POST.get("switch_setup_id")
        switch_remark = request.POST.get("switch_remark")
        switch_type_name = SwitchType.objects.get(id=switch_id)
        Switch.objects.create(
            switch_type_name = switch_type_name,
            switch_name = switch_name,
         #   switch_model = switch_model, 
            switch_serial_number = switch_serial_number,
            switch_po_number = switch_po_number,
            switch_po_date = switch_po_date,
            switch_vendor = switch_vendor, 
            switch_invoice = switch_invoice,
            switch_bond = switch_bond,
            switch_bond_number = switch_bond_number,
            switch_type = switch_type, 
            switch_ship_date = switch_ship_date,
            switch_arrival_date = switch_arrival_date,
            switch_warranty = switch_warranty,
            switch_added_byuser = switch_added_byuser,
            switch_added_ondate = switch_added_ondate,
            switch_ownership = switch_ownership,
            switch_ip_address = switch_ip_address,
            switch_hostname = switch_hostname,
            switch_mgmt_mac = switch_mgmt_mac ,
            switch_lan_mac = switch_lan_mac ,
            switch_os = switch_os,
            switch_fversion = switch_fversion,
            switch_hardware_revision = switch_hardware_revision,
            switch_setup_id = switch_setup_id,
            switch_remark = switch_remark,

        )
        return render(
            request,
            "add_switch.html",
            {
                'switch_tn':SwitchType.objects.all(),
                'msg':'switch Added!'

            }
        )        
    else:
         return render(
             request,
             "add_switch.html",
             {
                 'switch_tn':SwitchType.objects.all()
             }
           )
    
    return render(request, 'add_switch.html')



def add_laptop_type(request):
    if request.method == "POST":
        laptop_type_name = request.POST.get('laptop_type_name')
        laptop_make = request.POST.get('laptop_make')
        laptop_model = request.POST.get('laptop_model')
        laptop_processor = request.POST.get('laptop_processor')
        laptop_ram = request.POST.get('laptop_ram')
        laptop_hdd_model = request.POST.get('laptop_hdd_model')
        laptop_hdd_size = request.POST.get('laptop_hdd_size')
        laptop_display_size = request.POST.get('laptop_display_size')

        LaptopType.objects.create(
            laptop_type_name=laptop_type_name , 
            laptop_make=laptop_make , 
            laptop_model=laptop_model , 
            laptop_processor=laptop_processor , 
            laptop_ram = laptop_ram,
            laptop_hdd_model = laptop_hdd_model , 
            laptop_hdd_size = laptop_hdd_size, 
            laptop_display_size=laptop_display_size, 

        )
        return render(
            request,
            "add_laptop_type.html",

        )
    else:
        return render(
            request,
            "add_laptop_type.html",

        )

def add_laptop(request):
    if request.method == "POST":
        laptop_id = request.POST.get("laptop_type_name")
        laptop_type_name = LaptopType.objects.get(id=laptop_id)
       # laptop_model = request.POST.get("laptop_model")
        laptop_name = request.POST.get("laptop_name")
        laptop_serial_number = request.POST.get("laptop_serial_number")
        laptop_po_number = request.POST.get("laptop_po_number")
        laptop_po_date = request.POST.get("laptop_po_date")
        laptop_vendor = request.POST.get("laptop_vendor")
        laptop_invoice = request.POST.get("laptop_invoice")
        laptop_bond = request.POST.get("laptop_bond")
        laptop_bond_number = request.POST.get("laptop_bond_number")
        laptop_type = request.POST.get("laptop_type")
        laptop_ship_date = request.POST.get("laptop_ship_date")
        laptop_arrival_date = request.POST.get("laptop_arrival_date")
        laptop_warranty = request.POST.get("laptop_warranty")
        laptop_added_byuser = request.POST.get("laptop_added_byuser")
        laptop_added_ondate = request.POST.get("laptop_added_ondate")
        laptop_ownership = request.POST.get("laptop_ownership")
        laptop_ip_address = request.POST.get("laptop_ip_address")
        laptop_hostname = request.POST.get("laptop_hostname")
        laptop_mgmt_mac = request.POST.get("laptop_mgmt_mac")
        laptop_lan_mac = request.POST.get("laptop_lan_mac")
        laptop_os = request.POST.get("laptop_os")
        laptop_fversion = request.POST.get("laptop_fversion")
        laptop_hardware_revision = request.POST.get("laptop_hardware_revision")
        laptop_setup_id = request.POST.get("laptop_setup_id")
        laptop_remark = request.POST.get("laptop_remark")
        laptop_type_name = LaptopType.objects.get(id=laptop_id)
        Laptop.objects.create(
            laptop_type_name = laptop_type_name,
            laptop_name = laptop_name,
         #   laptop_model = laptop_model, 
            laptop_serial_number = laptop_serial_number,
            laptop_po_number = laptop_po_number,
            laptop_po_date = laptop_po_date,
            laptop_vendor = laptop_vendor, 
            laptop_invoice = laptop_invoice,
            laptop_bond = laptop_bond,
            laptop_bond_number = laptop_bond_number,
            laptop_type = laptop_type, 
            laptop_ship_date = laptop_ship_date,
            laptop_arrival_date = laptop_arrival_date,
            laptop_warranty = laptop_warranty,
            laptop_added_byuser = laptop_added_byuser,
            laptop_added_ondate = laptop_added_ondate,
            laptop_ownership = laptop_ownership,
            laptop_ip_address = laptop_ip_address,
            laptop_hostname = laptop_hostname,
            laptop_mgmt_mac = laptop_mgmt_mac ,
            laptop_lan_mac = laptop_lan_mac ,
            laptop_os = laptop_os,
            laptop_fversion = laptop_fversion,
            laptop_hardware_revision = laptop_hardware_revision,
            laptop_setup_id = laptop_setup_id,
            laptop_remark = laptop_remark,

        )
        return render(
            request,
            "add_laptop.html",
            {
                'laptop_tn': LaptopType.objects.all(),
                'msg':'laptop Added!'

            }
        )        
    else:
         return render(
             request,
             "add_laptop.html",
             {
                 'laptop_tn':LaptopType.objects.all()
             }
           )
    
    return render(request, 'add_laptop.html')

