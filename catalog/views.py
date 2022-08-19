from django.shortcuts import render
from django.http import HttpResponse

from .models import Catalog, Seller


def index(request):
    cat = Catalog.objects.all()
    sellers = Seller.objects.all()

    context = {
        'catal': cat, 
        'title': 'Список объявлений',
        'sellers': sellers,
        }
    return render(request, 'catalog\index.html', context=context)

def get_seller(request, seller_id):
    cat = Catalog.objects.filter(seller_id=seller_id)
    sellers = Seller.objects.all()
    seller = Seller.objects.get(pk = seller_id)
    context = {
        'catal': cat, 
        'sellers': sellers,
        'title': 'Список объявлений',
        'seller': seller,
        }
    # print (seller)
    return render(request, template_name = 'catalog/sellers.html', context=context)