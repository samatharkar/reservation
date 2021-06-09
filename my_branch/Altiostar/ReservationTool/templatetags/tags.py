from django import template


register = template.Library()

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