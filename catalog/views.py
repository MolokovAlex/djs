from django.shortcuts import render
from django.http import HttpResponse

from .models import Catalog


def index(request):
    # print (request)
    cat = Catalog.objects.all()

    # res = '<h1>Список Компонентов</h1>'
    # for item in cat:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.name}</p>\n</div>\n<hr>\n'
    # # return HttpResponse('Hello world')
    # return HttpResponse(res)
    context = {'catal': cat, 'title': 'Список'}
    return render(request, 'catalog\index.html', context=context)

# def test(request):
#     return HttpResponse('<h1>Тестовая страеница</h1>')