from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Fetches the value from a dictionary using the given key."""
    return dictionary.get(key)
