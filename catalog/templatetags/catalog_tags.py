from atexit import register
from django import template

from catalog.models import Seller

register = template.Library()

@register.simple_tag(name = 'get_list_sellers')
def get_sellers():
    return Seller.objects.all()

@register.inclusion_tag('catalog/list_sellers.html')
def show_sellers(arg1 = "Hello", arg2 = "world"):
    sellers = Seller.objects.all()
    return {"list_of_sellers" : sellers, 'arg1': arg1, 'arg2': arg2}