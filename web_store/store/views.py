from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

# Create your views here.

# menu = ['About', 'Categories', 'Personal account', 'Cart']
menu = [
    {'title': 'Главная', 'url_name': 'index'},
    {'title': 'Доставка', 'url_name': 'about_delivery'},
    {'title': 'Оплата', 'url_name': 'about_payment'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Частые вопросы', 'url_name': 'faq'},
    {'title': 'Личный кабинет', 'url_name': 'personal_account'},
    {'title': 'Корзина', 'url_name': 'cart'},
    {'title': 'Категория', 'url_name': 'category'},
    {'title': 'Телефон', 'url_name': 'phone'},
]


def index(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'store/index.html', context=context)


def about(request):
    return render(request, 'store/about.html', {'menu': menu, 'title': 'About'})


def about_delivery(request):
    return HttpResponse('Условия доставки')


def about_delivery(request):
    return HttpResponse('Условия доставки')


def about_payment(request):
    return HttpResponse('Условия оплаты')


def faq(request):
    return HttpResponse('Частые вопросы')


def personal_account(request):
    return HttpResponse('Личный кабинет')


def cart(request):
    return HttpResponse('Корзина')


def category(request):
    return HttpResponse('Категория')


def phone(request):
    return HttpResponse('Телефон')

def case_page(request, case_id):
    return HttpResponse(f'Карточка чехла с id = {case_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
