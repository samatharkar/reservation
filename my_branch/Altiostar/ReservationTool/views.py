from django.shortcuts import render, HttpResponse
from django.http import Http404, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *
import csv
from .filters import SetupFilter
from .filters import DeviceFilter


NAMES = {
    'DeviceType': 'device types',
    'Vendor': 'vendors',
    'Consumable': 'consumables',
    'Team': 'teams',
    'SetupType': 'setup types',
    'Setup': 'setups',
    'Device': 'devices',
}

TITLES = {
    'DeviceType': 'Device Type',
    'Vendor': 'Vendor',
    'Consumable': 'Consumable',
    'Team': 'Team',
    'SetupType': 'Setup Type',
    'Setup': 'Setup',
    'Device': 'Device',
}


# Create your views here.
def home(request):
	return render(request, 'home.html')


def login(request):
    pass
    return render(request, 'login.html')


def view_messages(request):
    if request.is_ajax():
        message_type = request.GET.get('message_type')
        message = request.GET.get('message')
        if message_type and message:
            if message_type == 'success':
                messages.success(request, message)
            elif message_type == 'danger':
                messages.danger(request, message)
        return render(request, 'messages.html')
    return Http404()


def add_device_type(request):
    if request.method == "POST":
        device_type_form = DeviceTypeForm(request.POST)
        print(request.POST)
        print(device_type_form)
        if device_type_form.is_valid():
            device_type_form.save()
            messages.success(request, f'Device Type Added!')
    else:
        device_type_form = DeviceTypeForm()
    return render(request, 'add_device_type.html', {
                'device_type_form': device_type_form,
            }
        )


def vendor(request):
    vendor_list = Vendor.objects.all()
    field_names = Vendor._meta.fields[1:]
    return render(request, 'vendor.html', {
                'title': TITLES['Vendor'],
                'name_plural': NAMES['Vendor'],
                'vendor_list': vendor_list,
                'field_names': field_names,
            }
        )


def load_vendor_form(request):
    if request.is_ajax():
        mode = request.GET.get('mode')
        if mode == 'add':
            vendor_form = VendorForm()
        elif mode == 'modify':
            id = request.GET.get('id')
            current_vendor = Vendor.objects.get(id=id)
            vendor_form = VendorForm(instance=current_vendor)
        return render(request, 'dashboard_modal_content_template.html', {
                    'add_or_modify_url': reverse('add_or_modify_vendor'),
                    'title': TITLES['Vendor'],
                    'mode': mode,
                    'add_or_modify_form': vendor_form,
                }
            )
    return Http404()


def add_or_modify_vendor(request):
    if request.is_ajax():
        if request.method == "POST":
            completed = False
            vendor_form = VendorForm(request.POST)
            if vendor_form.is_valid():
                vendor_form.save()
                completed = True
        return JsonResponse({
                'completed': completed
            }
        )
    return Http404()


def view_vendor(request):
    if request.is_ajax():
        vendor_list = Vendor.objects.all()
        field_names = Vendor._meta.fields[1:]
        return render(request, 'dashboard_body_template.html', {
                'object': NAMES['Vendor'],
                'list': vendor_list,
                'field_names': field_names,
            })
    return Http404()


def search_vendor(request):
    if request.is_ajax():
        search_text = request.GET.get('search_text')
        vendor_list = Vendor.objects.filter(
                            Q(name__istartswith = search_text)
                        )
        field_names = Vendor._meta.fields[1:]
        if len(vendor_list):
            return render(request, 'dashboard_body_template.html', {
                    'object': NAMES['Vendor'],
                    'list': vendor_list,
                    'field_names': field_names,
                })
        else:
            return HttpResponse('')
    return Http404()


def delete_vendor(request):
    if request.is_ajax():
        id_list = request.POST.getlist('id_list[]')
        vendor_list = Vendor.objects.filter(
                            id__in=id_list,
                            devices__isnull=True,
                        )
        deleted_count = len(vendor_list)
        not_deleted_count = len(id_list) - deleted_count
        vendor_list.delete()
        return JsonResponse({
                    'deleted_count': deleted_count,
                    'not_deleted_count': not_deleted_count
                }
            )
    return Http404()


def add_consumable(request):
    if request.method == "POST":
        consumable_form = ConsumableForm(request.POST)
        if consumable_form.is_valid():
            consumable_form.save()
            messages.success(request,f'Consumable Added!')
    else:
        consumable_form = ConsumableForm()
    return render(request, 'add_consumable.html', {
                'consumable_form': consumable_form,
            }
        )


def add_team(request):
    if request.method == "POST":
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            team_form.save()
            messages.success(request,f'Team Added!')
    else:
        team_form = TeamForm()
    return render(request, 'add_team.html', {
                'team_form': team_form,
            }
        )


def add_device(request):
    if request.method == "POST":
        device_form = DeviceForm(request.POST)
        if device_form.is_valid():
            device_form.save()
            messages.success(request,f'Device Added!')
    else:
        device_form = DeviceForm()
    return render(request, 'add_device.html',{
                'device_form': device_form,
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
        setup_type_form = SetupTypeForm(request.POST)
        if setup_type_form.is_valid():
            setup_type_form.save()
            messages.success(request,f'Setup Type Added!')
    else:
        setup_type_form = SetupTypeForm()
    return render(request, 'add_setup_type.html', {
                'setup_type_form': setup_type_form,
            }
        )


def make_setup(request):
    if request.method == "POST":
        setup_form = MakeSetupForm(request.POST)
        device_id_list = request.POST.getlist('device_id_list[]')
        if setup_form.is_valid():
            setup = setup_form.save()
            device_list = Device.objects.filter(
                        id__in=device_id_list
                    )
            for device in device_list:
                setup.devices.add(device)
            messages.success(request,f'Setup Formed!')
    else:
        setup_form = MakeSetupForm()
    device_type_list = DeviceType.objects.all()
    return render(request, 'make_setup.html', {
                'form': setup_form,
                'device_type_list': device_type_list,
            }
        )

def search_devices_for_setup(request):
    if request.is_ajax():
        id_list = request.GET.getlist('device_type_id_list[]')
        device_type_list = DeviceType.objects.filter(
                            id__in=id_list
                        )
        device_list = Device.objects.none()
        for device_type in device_type_list:
            device_list |= device_type.devices.filter(setup__isnull=True)
        return render(request, 'device_list_modal.html', { 
                    'device_list': device_list, 
                }
            )
    return Http404()


def add_devices_to_setup(request):
    if request.is_ajax():
        id_list = request.GET.getlist('device_id_list[]')
        added_device_list = Device.objects.filter(
                            id__in=id_list
                        )
        return render(request, 'added_devices_to_setup.html', { 
                    'added_device_list': added_device_list, 
                }
            )
    return Http404()


def view_setup(request):
    context = {}
    setup_entries = Setup.objects.all()
    context['setup_entries'] = setup_entries
    return render(request, 'view_setup.html', context)



def search_setup(request):
    setup_list = Setup.objects.all()
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