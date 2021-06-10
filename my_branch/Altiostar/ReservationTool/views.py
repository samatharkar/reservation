from django.shortcuts import render, HttpResponse
from django.http import Http404, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *
from .search_helpers import *
import csv
import datetime


# Dictionary of models and their names
PLURAL_NAMES = {
    'DeviceType': 'device types',
    'Vendor': 'vendors',
    'Consumable': 'consumables',
    'Team': 'teams',
    'SetupType': 'setup types',
    'Setup': 'setups',
    'Device': 'devices',
}

# Dictionary of models and their titles
TITLES = {
    'DeviceType': 'Device Type',
    'Vendor': 'Vendor',
    'Consumable': 'Consumable',
    'Team': 'Team',
    'SetupType': 'Setup Type',
    'Setup': 'Setup',
    'Device': 'Device',
}

# Dictionary of models and their class instances
MODELS = {
    'DeviceType': DeviceType,
    'Vendor': Vendor,
    'Consumable': Consumable,
    'Team': Team,
    'SetupType': SetupType,
    'Setup': Setup,
    'Device': Device,
}

# Dictionary of models and their model form function instances
FORMS = {
    'DeviceType': DeviceTypeForm,
    'Vendor': VendorForm,
    'Consumable': ConsumableForm,
    'Team': TeamForm,
    'SetupType': SetupTypeForm,
    'Setup': MakeSetupForm,
    'Device': DeviceForm,
}

# Dictionary of models and csv export file names
FILE_NAMES = {
    'DeviceType': 'device_types',
    'Vendor': 'vendors',
    'Consumable': 'consumables',
    'Team': 'teams',
    'SetupType': 'setup_types',
    'Setup': 'setups',
    'Device': 'devices',
}

# Home
def home(request):
	return render(request, 'home.html')

# Login
def login(request):
    pass
    return render(request, 'login.html')

# Rendering the messages on top of the page
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

# Dashboard of any model
def dashboard(request, name):
    object_list = MODELS[name].objects.all()
    field_names = MODELS[name]._meta.fields[1:]
    context = {
                'title': TITLES[name],
                'object': PLURAL_NAMES[name],
                'list': object_list,
                'field_names': field_names,
                'load_form_url': reverse('load_object_form', args=[name]),
                'add_or_modify_url': reverse('add_or_modify_object', args=[name]),
                'view_url': reverse('view_objects', args=[name]),
                'search_url': reverse('search_objects', args=[name]),
                'delete_url': reverse('delete_objects', args=[name]),
            }
    return render(request, 'dashboard_template.html', context)

# Load the form dynamically of any model
def load_object_form(request, name):
    if request.is_ajax():
        mode = request.GET.get('mode')
        if mode == 'add':
            object_form = FORMS[name]()
        elif mode == 'modify':
            id = request.GET.get('id')
            current_object = MODELS[name].objects.get(id=id)
            object_form = FORMS[name](instance=current_object)
        context = {
                    'add_or_modify_url': reverse('add_or_modify_object', args=[name]),
                    'title': TITLES[name],
                    'mode': mode,
                    'add_or_modify_form': object_form,
                }
        # If the request is from Setup dashboard, handle the adding devices feature
        if name == 'Setup':
            device_type_list = DeviceType.objects.all()
            context['device_type_list'] = device_type_list
            if mode == 'modify':
                device_list = current_object.devices.all()
                context['device_list'] = device_list
        return render(request, 'dashboard_modal_content_template.html', context)
    return Http404()

# Add/Modify objects of any model
def add_or_modify_object(request, name):
    if request.is_ajax():
        if request.method == "POST":
            mode = request.POST.get('mode')
            completed = False
            if mode == 'add':
                object_form = FORMS[name](request.POST)
            elif mode == 'modify':
                id = request.POST.get('id')
                current_object = MODELS[name].objects.get(id=id)
                object_form = FORMS[name](request.POST, instance=current_object)
            if object_form.is_valid():
                if name == 'Setup':
                    setup = object_form.save()
                    device_id_list = request.POST.getlist('device_id_list[]')
                    device_list = Device.objects.filter(
                                id__in=device_id_list
                            )
                    for device in device_list:
                        setup.devices.add(device)
                else:
                    object_form.save()
                completed = True
            response = {
                'completed': completed
            }
            return JsonResponse(response)
    return Http404()

# View objects of any model
def view_objects(request, name):
    if request.is_ajax():
        object_list = MODELS[name].objects.all()
        field_names = MODELS[name]._meta.fields[1:]
        if name == 'Device' or name == 'Setup':
            template = 'dashboard_body_template_special.html'
        else:
            template = 'dashboard_body_template.html'
        context = {
                'object': PLURAL_NAMES[name],
                'list': object_list,
                'field_names': field_names,
            }
        return render(request, template, context)
    return Http404()

# Search objects of any model
def search_objects(request, name):
    if request.is_ajax():
        search_text = request.GET.get('search_text')
        object_list = None
        if name == 'Device' or name == 'Setup':
            search_by = request.GET.get('search_by')
            if name == 'Device':
                object_list = search_helper_devices(search_by, search_text)
            else:
                object_list = search_helper_setups(search_by, search_text)
        else:
            object_list = MODELS[name].objects.filter(
                                name__icontains = search_text
                            )
        field_names = MODELS[name]._meta.fields[1:]
        if name == 'Device' or name == 'Setup':
            template = 'dashboard_body_template_special.html'
        else:
            template = 'dashboard_body_template.html'
        context = {
                    'object': PLURAL_NAMES[name],
                    'list': object_list,
                    'field_names': field_names,
                }
        if len(object_list):
            return render(request, template, context)
        else:
            return HttpResponse('')
    return Http404()

# Delete objects of any model
def delete_objects(request, name):
    if request.is_ajax():
        id_list = request.POST.getlist('id_list[]')
        object_list = MODELS[name].objects.first()
        try:
            # Check if the object passed has a foreignkey with Device model
            object_list.devices.exists()
        except:
            try:
                # Check if the object passed has a foreignkey with Setup model
                object_list.setups.exists()
            except:
                # Exception occured meaning an object not related to both Device & Setup 
                # model found, hence the object is of Device Model
                object_list = MODELS[name].objects.filter(
                                id__in=id_list,
                            )
            else:
                # Safely executed meaning an object related to Setup model found
                object_list = MODELS[name].objects.filter(
                                id__in=id_list,
                                setups__isnull=True,
                            )
            
        else:
            # Safely executed meaning an object related to Device model found
            object_list = MODELS[name].objects.filter(
                                id__in=id_list,
                                devices__isnull=True,
                            )
            
        deleted_count = len(object_list)
        not_deleted_count = len(id_list) - deleted_count
        object_list.delete()
        response = {
                    'deleted_count': deleted_count,
                    'not_deleted_count': not_deleted_count
                }
        return JsonResponse(response)
    return Http404()

# Export data
def export_objects(request, name):
    current_time = datetime.datetime.now().strftime('%d-%m-%y_%I-%M-%p')
    filename = f'{FILE_NAMES[name]}_{str(current_time)}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    writer = csv.writer(response)
    field_names = MODELS[name]._meta.fields[1:]
    field_names = [field.verbose_name for field in field_names]
    values = MODELS[name].objects.all().values_list()
    # If the model is Setup, make changes to append the list of devices attached
    if name == 'Setup':
        values = list(values)
        field_names.append('All Devices')
        setups = Setup.objects.all()
        for i, setup in enumerate(setups):
            devices = setup.devices.all()
            devices = ', '.join([device.name for device in devices])
            devices = '"' + devices + '"'
            values[i] = list(values[i])
            values[i].append(devices)
    writer.writerow(field_names)
    for row in values:
        writer.writerow(row[1:])
    return response

# Render device(s) based on the device type(s) searched in the modal of a dashboard
def search_devices_for_setup(request):
    if request.is_ajax():
        id_list = request.GET.getlist('device_type_id_list[]')
        do_not_inlcude_id_list = request.GET.getlist('do_not_include_list[]')
        device_type_list = DeviceType.objects.filter(
                            id__in=id_list
                        )
        print(do_not_inlcude_id_list)
        print(id_list)
        device_list = Device.objects.none()
        for device_type in device_type_list:
            device_list |= device_type.devices.filter(setup__isnull=True)
        device_list = device_list.exclude(id__in=do_not_inlcude_id_list)
        if len(device_list):
            context = { 
                        'device_list': device_list, 
                    }
            return render(request, 'device_list_on_search.html', context)
        else:
            return HttpResponse('')
    return Http404()

# Attach the added devices with the Setup form as hidden inputs
def add_devices_to_setup(request):
    if request.is_ajax():
        id_list = request.GET.getlist('device_id_list[]')
        added_device_list = Device.objects.filter(
                            id__in=id_list
                        )
        context = { 
                    'added_device_list': added_device_list, 
                }
        return render(request, 'device_added_list.html', context)
    return Http404()

# Remove the attached devices from the Setup 
def remove_devices_from_setup(request):
    if request.is_ajax():
        id = request.GET.get('id')
        completed = False
        try:
            device = Device.objects.get(id=id)
        except:
            pass
        else:
            if device.setup:
                device.setup = None
                device.save()
            completed = True
        response = {
                    'completed': completed
                }
        return JsonResponse(response)
    return Http404()