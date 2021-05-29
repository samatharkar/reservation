from django.shortcuts import render, HttpResponse
from django.http import Http404, JsonResponse
from django.contrib import messages
from ReservationTool.models import Device
from .models import *
from .forms import *
import csv
from .filters import SetupFilter
from .filters import DeviceFilter


# Create your views here.
def home(request):
	return render(request, "home.html")


def login(request):
    pass
    return render(request, 'login.html')


def add_device_type(request):
    if request.method == "POST":
        device_type_form = AddDeviceTypeForm(request.POST)
        if device_type_form.is_valid():
            device_type_form.save()
            messages.success(request,f'Device Type Added!')
    else:
        device_type_form = AddDeviceTypeForm()
    return render(request, "add_device_type.html", {
            'device_type_form': device_type_form,
        }
    )


def add_vendor(request):
    if request.method == "POST":
        vendor_form = AddVendorForm(request.POST)
        if vendor_form.is_valid():
            vendor_form.save()
            messages.success(request,f'Device Type Added!')
    else:
        vendor_form = AddVendorForm()
    return render(request, "add_vendor.html", {
            'vendor_form': vendor_form,
        }
    )


def add_consumable(request):
    if request.method == "POST":
        consumable_form = AddConsumableForm(request.POST)
        if consumable_form.is_valid():
            consumable_form.save()
            messages.success(request,f'Device Type Added!')
    else:
        consumable_form = AddConsumableForm()
    return render(request, "add_consumable.html", {
            'consumable_form': consumable_form,
        }
    )


def add_team(request):
    if request.method == "POST":
        team_form = AddTeamForm(request.POST)
        if team_form.is_valid():
            team_form.save()
            messages.success(request,f'Device Type Added!')
    else:
        team_form = AddTeamForm()
    return render(request, "add_team.html", {
            'team_form': team_form,
        }
    )


def add_device(request):
    if request.method == "POST":
        device_form = AddDeviceForm(request.POST)
        if device_form.is_valid():
            device_form.save()
            messages.success(request,f'Device Type Added!')
    else:
        device_form = AddDeviceForm()
    #     name = request.POST.get('name')
    #     type_id = request.POST.get('type')
    #     type = DeviceType.objects.get(id=type_id)
    #     srno = request.POST.get('srno')
    #     po_number = request.POST.get('po_number')
    #     po_date = request.POST.get('po_date')
    #     vendor_id = request.POST.get('vendor')
    #     vendor = Vendor.objects.get(id=vendor_id)
    #     invoice_number = request.POST.get('invoice_number')
    #     bonded = request.POST.get('bonded')
    #     bond_number = request.POST.get('bond_number')
    #     shipped_date = request.POST.get('shipped_date')
    #     arrival_date = request.POST.get('arrival_date')
    #     warranty_inmonths = request.POST.get('warranty_inmonths')
    #     added_byuser = request.POST.get('added_byuser')
    #     added_date = request.POST.get('added_date')
    #     ownership = request.POST.get('ownership')
    #     remark = request.POST.get('remark')
        
    #     Device.objects.create(
    #         name = name , 
    #         type = type ,
    #         srno=srno , 
    #         po_number=po_number , 
    #         po_date=po_date , 
    #         vendor=vendor , 
    #         invoice_number=invoice_number,
    #         bonded=bonded,
    #         bond_number=bond_number,
    #         shipped_date=shipped_date,
    #         arrival_date=arrival_date,
    #         warranty_inmonths=warranty_inmonths,
    #         added_byuser=added_byuser,
    #         added_date=added_date,
    #         ownership=ownership,
    #         remark=remark

    #     )
    #     return render(
    #         request,
    #         "add_device.html",
    #         {
    #             'vendors':Vendor.objects.all(),
    #             'd_type':DeviceType.objects.all(),
    #             'msg':'Vendor Added!'
    #         }
    #     )  
        
    # else:
    return render(request, "add_device.html",{
            'device_form': device_form,
            'vendors':Vendor.objects.all(),
            'd_type':DeviceType.objects.all(),
        }
    )


def view_device(request):
    context = {}
    entries = Device.objects.all()
    context['entries'] = entries
    return render(request, 'view_device.html', context)


def search_device(request):
     device_list = Device.objects.all()
     device_filter = DeviceFilter(request.GET, queryset=device_list)
     return render(request, 'search_device.html', {'filter': device_filter })


def add_setup_type(request):
    if request.method == "POST":
        setup_type_form = AddSetupTypeForm(request.POST)
        if setup_type_form.is_valid():
            setup_type_form.save()
            messages.success(request,f'Device Type Added!')
    else:
        setup_type_form = AddSetupTypeForm()
    return render(request, "add_setup_type.html", {
            'setup_type_form': setup_type_form,
        }
    )


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


def view_setup(request):
    context = {}
    setup_entries = CreateSetup.objects.all()
    context['setup_entries'] = setup_entries
    return render(request, 'view_setup.html', context)



def search_setup(request):
    setup_list = MakeSetup.objects.all()
    setup_filter = SetupFilter(request.GET, queryset=setup_list)
    return render(request, 'search_setup.html', {'filter': setup_filter })


def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fields.csv"'


    writer = csv.writer(response)
    writer.writerow(['Hostname', 'IP', 'MAC', 'Device Type', 'Serial Number', 'Make/Model'])

    for fields in Device.objects.all().values_list('hostname', 'ip', 'mac', 'device_type','serial_number', 'make'):
        writer.writerow(fields)

    return response