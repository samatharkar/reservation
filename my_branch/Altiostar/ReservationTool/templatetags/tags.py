from django import template


register = template.Library()


@register.filter
def get_tag(tags):
    return 'danger' if tags == 'error' else tags


@register.filter
def get_field_value(object, field):
    return getattr(object, field)