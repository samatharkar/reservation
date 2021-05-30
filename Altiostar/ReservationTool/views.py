from django.shortcuts import redirect, render, HttpResponse
from ReservationTool.models import Device
from django.contrib.auth import authenticate, login, logout
from .models import *
import csv
from .filters import SetupFilter
from django.contrib import messages

from .filters import DeviceFilter


# Create your views here.
def home(request):
	return render(request, "home.html", {})


def add_setup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        remark = request.POST.get("remark")

        CreateSetup.objects.create(
            name = name,
            remark = remark

        )
        return render(
            request,
            "add_setup.html",
            {
                'msg':'Setup Added!'

            }
        )        
    else:
         return render(
             request,
             "add_setup.html"

           )

def add_device(request):
    if request.method == "POST":
        name = request.POST.get('name')
        type_id = request.POST.get('type')
        type = DeviceType.objects.get(id=type_id)
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
                'msg':'Vendor Added!'
            }
        )  
        
    else:
        return render(
            request,
            "add_device.html",

            {
                'vendors':Vendor.objects.all(),
                'd_type':DeviceType.objects.all(),

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

def add_team(request):
    if request.method == "POST":
        name = request.POST.get("name")
        manager = request.POST.get("manager")
        remark = request.POST.get("remark")
        
        Team.objects.create(
            name = name,
            manager = manager, 
            remark = remark
        )
        return render(
            request,
            "add_team.html",
            {
             'msg':'Team Added!'

            }
            

        )        
    else:
         return render(
             request,
             "add_team.html",

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

def add_setup_type(request):
    if request.method == "POST":
        setup_type = request.POST.get("setup_type")
        remark = request.POST.get("remark")
        
        SetupType.objects.create(
            setup_type = setup_type,
            remark = remark
        )
        return render(
            request,
            "add_setup_type.html",
            {
             'msg':'Setup Type Added!'

            }
            

        )        
    else:
         return render(
             request,
             "add_setup_type.html",

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
        setup_type_id = request.POST.get("setup_type")
        setup_type = SetupType.objects.get(id = setup_type_id)
        booked_by_id = request.POST.get("booked_by")
        booked_by = Team.objects.get(id = booked_by_id)

        MakeSetup.objects.create(
            name = name,
            device = device,
            consumable = consumable,
            type = type,
            booked_by = booked_by,
            setup_type = setup_type

        )
        return render(
            request,
            "make_setup.html",
            {
                'device_n':Device.objects.all(),
                'booked_team':Team.objects.all(),
                'booked_team':Team.objects.all(),
                'setup_type_n':SetupType.objects.all(),
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
                'consumable_n':Consumable.objects.all(),
                'type_n':DeviceType.objects.all(),

            }
            
           )

def view_device(request):
    context = {}
    entries = Device.objects.all()
    context['entries'] = entries
    return render(request, 'view_device.html', context)



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
    setup_list = MakeSetup.objects.all()
    setup_filter = SetupFilter(request.GET, queryset=setup_list)
    return render(request, 'search_setup.html', {'filter': setup_filter })

def search_device(request):
     device_list = Device.objects.all()
     device_filter = DeviceFilter(request.GET, queryset=device_list)
     return render(request, 'search_device.html', {'filter': device_filter })

def userlogin(request):
    if request.method == 'POST':
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:

            login(request, user)
            messages.success(request, "Logged in")
            return redirect('login')
        else:
            messages.error(request, "Wrong Creds")
            return redirect('login')


    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('login')