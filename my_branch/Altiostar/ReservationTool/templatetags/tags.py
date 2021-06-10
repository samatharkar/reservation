from django import template

register = template.Library()

SEARCH_ALLOWED = {
	'Device': [
		'name', 
		'type', 
		'srno', 
		'po_number', 
		'vendor', 
		'invoice_number', 
		'bond_number',
		'setup',
        'added_byuser',
        'ownership',
        'remark',
	],
	'Setup': [
		'name',
        'setup_type',
        'consumable',
        'booked_by',
        'remark', 
	]
}

# Convert django messages to bootstrap class
@register.filter
def get_tag(tags):
    return 'danger' if tags == 'error' else tags

# Get the value of a field of a particular model's instance
@register.filter
def get_field_value(object, field):
    return getattr(object, field)

# Get the list of devices attached to a setup
@register.filter
def get_device_list(setup):
	return setup.devices.all()

# Check if the search is allowed by this mode
@register.filter
def search_allowed(mode, title):
	if mode.name in SEARCH_ALLOWED[title]:
		return True
	else:
		return False