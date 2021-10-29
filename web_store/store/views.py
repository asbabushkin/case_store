from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

menu = ['About', 'Categories', 'Personal account', 'Cart']

def index(request):
    cats = Category.objects.all()
    return render(request, 'store/index.html', {'cats': cats, 'menu': menu, 'title': 'Main Page'})

def about(request):
    return render(request, 'store/about.html', {'menu': menu, 'title': 'About'})


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