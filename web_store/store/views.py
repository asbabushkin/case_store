import logging
from itertools import chain

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import *
from cart.forms import CartAddProductForm
# Create your views here.

logger = logging.getLogger(__name__)

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
    {'title': 'Логин', 'url_name': 'login'},
]


class StoreHome(ListView):
    model = Product
    form_filter = ProductFilterForm
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['phone_brands'] = list(Phone.objects.values_list('brand', flat=True).distinct().order_by('brand'))
        context['phones'] = Phone.objects.all()
        context['img_collection'] = Property.objects.all()
        context['title'] = 'Главная страница'
        context['form_filter'] = ProductFilterForm
        logger.info('Main page downloaded!')
        return context

    def get_queryset(self):
        form = self.form_filter(self.request.GET)
        if form.is_valid():
            products = []
            products_phone = []
            products_plastic = []
            products_shockproof = []
            products_silicon = []
            products_animals = []
            products_cartoons = []
            products_games = []
            products_anime = []
            products_labels = []
            phone_id_list = []
            if form.cleaned_data['phone_name'] or form.cleaned_data['cat_plastic'] or form.cleaned_data[
                'cat_shockproof'] or form.cleaned_data['cat_silicon'] or form.cleaned_data['col_animals'] or form.cleaned_data['col_cartoons'] or \
                    form.cleaned_data['col_games'] or form.cleaned_data['col_anime'] or form.cleaned_data['col_labels']:

                if form.cleaned_data['phone_name']:
                    #products_phone = ProductToPhone.objects.select_related('product_id', 'phone_id').filter(phone_id__model='iPhone11').values('product_id__pk', 'product_id__category_id', 'product_id__name', 'product_id__slug', 'product_id__image', 'product_id__description', 'product_id__price')
                    products_phone = ProductToPhone.objects.select_related('product_id', 'phone_id').filter(
                        phone_id__model=form.cleaned_data['phone_name']).values('product_id__pk')

                    for p in products_phone:
                        ph = p.get('product_id__pk')
                        phone_id_list.append(ph)

                    products_phone = Product.objects.filter(pk__in=phone_id_list)

                if form.cleaned_data['cat_plastic']:
                    products_plastic = Product.objects.filter(category_id__name='Чехол пластиковый')
                if form.cleaned_data['cat_shockproof']:
                    products_shockproof = Product.objects.filter(category_id__name='Чехол противоударный')
                if form.cleaned_data['cat_silicon']:
                    products_silicon = Product.objects.filter(category_id__name='Чехол силиконовый')
                if form.cleaned_data['col_animals']:
                    products_animals = Product.objects.filter(property__value='Животные')
                if form.cleaned_data['col_cartoons']:
                    products_cartoons = Product.objects.filter(property__value='Мультфильмы')
                if form.cleaned_data['col_games']:
                    products_games = Product.objects.filter(property__value='Игры')
                if form.cleaned_data['col_anime']:
                    products_anime = Product.objects.filter(property__value='Аниме')
                if form.cleaned_data['col_labels']:
                    products_labels = Product.objects.filter(property__value='Надписи')

                prod_cat = set(list(chain(products_plastic, products_shockproof, products_silicon)))
                prod_col = set(list(chain(products_animals, products_cartoons, products_games, products_anime, products_labels)))
                products_phone = set(products_phone)

                if len(prod_cat) == 0:
                    if len(prod_col) == 0:
                        if len(products_phone) > 0:
                            products = products_phone
                            print('только телефоны')
                    else:
                        if len(products_phone) > 0:
                            products =products_phone.intersection(prod_col)
                            print('телефоны и коллекции')
                        else:
                            products = prod_col
                            print('collections only')

                else:
                    if len(prod_col) > 0:
                        if len(products_phone) > 0:
                            products = prod_cat.intersection(prod_col, products_phone)
                            print('categories, collection, phones')
                        else:
                            products = prod_cat.intersection(prod_col)
                            print('categories, collections')
                    else:
                        if len(products_phone) > 0:
                            products = prod_cat.intersection(products_phone)
                            print('categories, phones')
                        else:
                            products = prod_cat
                            print('categories only')

                return products
            else:
                print('nothing')
                logger.warning('WARNING! No filters selected')
                return Product.objects.all()

class ProductPage(DetailView):
    model = Product
    template_name = 'store/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    cart_product_form = CartAddProductForm()
    #add_to_cart_form = AddToCartForm()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = context['product']
        context['product'] = context['product']
        context['menu'] = menu
        context['cart_product_form'] = CartAddProductForm
        logger.info('Product page downloaded')
        return context

#
# class CartPage(ListView):
#     model = Cart
#     template_name = 'store/cart.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = context['product']
#         context['menu'] = menu
#         context['add_to_cart_form'] = AddToCartForm
#         return context




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

def login(request):
    return HttpResponse('Войти')
