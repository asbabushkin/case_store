from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return HttpResponse('Страница приложения Магазин')


def categories(request, cat_id):
    if request.GET:
        print(request.GET)
    else:
        print('No request data')

    # if request.POST:
    #     print(request.POST)
    # else:
    #     print('No POST data')
    return HttpResponse(f"<h1>Страница категории</h1><p>{cat_id}</p>")

def archive(request, year):
    if int(year) > 2020:
        #raise Http404()
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')