from .models import Device, Setup

# Search helper to search for devices through different fields
def search_helper_devices(search_by, search_text):
    object_list = {
        'name': Device.objects.filter(name__icontains = search_text),
        'type': Device.objects.filter(type__name__icontains = search_text),
        'srno': Device.objects.filter(srno__icontains = search_text),
        'po_number': Device.objects.filter(po_number__icontains = search_text),
        'vendor': Device.objects.filter(vendor__name__icontains = search_text),
        'invoice_number': Device.objects.filter(invoice_number__icontains = search_text),
        'bond_number': Device.objects.filter(bond_number__icontains = search_text),
        'setup': Device.objects.filter(setup__name__icontains = search_text),
        'added_byuser': Device.objects.filter(added_byuser__icontains = search_text),
        'ownership': Device.objects.filter(ownership__icontains = search_text),
        'remark': Device.objects.filter(remark__icontains = search_text), 

    }
    return object_list[search_by]

# Search helper to search for setups through different fields
def search_helper_setups(search_by, search_text):
    object_list = {
        'name': Setup.objects.filter(name__icontains = search_text),
        'setup_type': Setup.objects.filter(setup_type__name__icontains = search_text),
        'consumable': Setup.objects.filter(consumable__name__icontains = search_text),
        'booked_by': Setup.objects.filter(booked_by__name__icontains = search_text),
        'remark': Setup.objects.filter(remark__icontains = search_text), 

    }
    return object_list[search_by]