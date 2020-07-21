from django import template

register = template.Library()

# This is just for the testing purpose of the user template filter
@register.filter(name='cut') # This line does the same work as the line commented below
def cut(value, arg):
    # This cuts out all value of arg form the stringa
    return value.replace(arg, '')

# register.filter('cut', cut)