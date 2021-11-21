from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *
from .forms import *
from django.db.models import Q
from itertools import chain

# Create your views here.

# class IndexPage():
#     model = Product


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
    phones = Phone.objects.all()
    products = Product.objects.all()
    img_collection = Value.objects.all()
    phone_brands = []
    for p in phones:
        if p.brand not in phone_brands:
            phone_brands.append(p.brand)
    phone_brands.sort()

    form_filter = ProductFilterForm(request.GET)
    if form_filter.is_valid():
        if form_filter.cleaned_data['cat_plastic'] or form_filter.cleaned_data['cat_shockproof'] or form_filter.cleaned_data['cat_silicon']:
            if form_filter.cleaned_data['cat_plastic']:
                products_plastic = products.filter(category_id__name='Чехол пластиковый')
            else:
                products_plastic = []
            if form_filter.cleaned_data['cat_shockproof']:
                products_shockproof = products.filter(category_id__name='Чехол противоударный')
            else:
                products_shockproof = []
            if form_filter.cleaned_data['cat_silicon']:
                products_silicon = products.filter(category_id__name='Чехол силиконовый')
            else:
                products_silicon = []
        products = list(chain(products_plastic, products_shockproof, products_silicon))

        # if form_filter.cleaned_data['min_price']:
        #     products = products.filter(price__gte=form_filter.cleaned_data['min_price'])
        # if form_filter.cleaned_data['max_price']:
        #     products = products.filter(price__lte=form_filter.cleaned_data['max_price'])
        # elif form_filter.cleaned_data['cat_plastic']:
        #     products = products.filter(category_id__name='Чехол пластиковый')
        #
        # # if form_filter.cleaned_data['cat_plastic'] or form_filter.cleaned_data['cat_shockproof'] or form_filter.cleaned_data['cat_silicon']:
        # #     products = products.filter(Q(category_id__name='Чехол пластиковый') | Q(category_id__name='Чехол противоударный') | Q(category_id__name='Чехол силиконовый')).distinct
        # elif form_filter.cleaned_data['cat_shockproof']:
        #     products = products.filter(category_id__name='Чехол противоударный')
        # elif form_filter.cleaned_data['cat_silicon']:
        #     products = products.filter(category_id__name='Чехол силиконовый')

    context = {
        'cats': cats,
        'phones': phones,
        'products': products,
        'img_collection': img_collection,
        'phone_brands': phone_brands,
        'menu': menu,
        'title': 'Главная страница',
        'form_filter': form_filter,
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
    return render(request, 'store/phone.html')

def product_page(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product,
        'category': product.category_id,

    }
    return HttpResponse(f'Карточка чехла с id = {product_slug}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
