from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import *
from .forms import *
from itertools import chain

# Create your views here.


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


class StoreHome(ListView):
    model = Product
    form_filter = ProductFilterForm
    template_name = 'store/index.html'
    context_object_name = 'products'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        phone_brands = list(Phone.objects.values_list('brand', flat=True))
        phone_brands = list(set(phone_brands))
        phone_brands.sort()


        context['phone_brands'] = phone_brands
        context['cats'] = Category.objects.values('name')
        context['phones'] = Phone.objects.all()
        context['img_collection'] = Value.objects.all()
        context['title'] = 'Главная страница'
        context['form_filter'] = ProductFilterForm
        return context

    def get_queryset(self):
        form = self.form_filter(self.request.GET)
        if form.is_valid():
            products_plastic = []
            products_shockproof = []
            products_silicon = []
            if form.cleaned_data['cat_plastic'] or form.cleaned_data['cat_shockproof'] or form.cleaned_data['cat_silicon']:
                if form.cleaned_data['cat_plastic']:
                    products_plastic = Product.objects.filter(category_id__name='Чехол пластиковый')
                if form.cleaned_data['cat_shockproof']:
                    products_shockproof = Product.objects.filter(category_id__name='Чехол противоударный')
                if form.cleaned_data['cat_silicon']:
                    products_silicon = Product.objects.filter(category_id__name='Чехол силиконовый')
                if form.cleaned_data['col_animals']:
                    products_animals = Product.objects.filter(category_id__name='Чехол силиконовый')


                products = list(chain(products_plastic, products_shockproof, products_silicon))

                return products
            # return Product.objects.filter(name__icontains=form.cleaned_data['name'])
            else:

                return Product.objects.all()






# функциональный подход
# def index(request):
#     cats = Category.objects.all()
#     phones = Phone.objects.all()
#     products = Product.objects.all()
#     img_collection = Value.objects.all()
#     phone_brands = []
#     for p in phones:
#         if p.brand not in phone_brands:
#             phone_brands.append(p.brand)
#     phone_brands.sort()
#
#     form_filter = ProductFilterForm(request.GET)
#     if form_filter.is_valid():
#         products_plastic = []
#         products_shockproof = []
#         products_silicon = []
#         if form_filter.cleaned_data['cat_plastic'] or form_filter.cleaned_data['cat_shockproof'] or form_filter.cleaned_data['cat_silicon']:
#             if form_filter.cleaned_data['cat_plastic']:
#                 products_plastic = products.filter(category_id__name='Чехол пластиковый')
#             if form_filter.cleaned_data['cat_shockproof']:
#                 products_shockproof = products.filter(category_id__name='Чехол противоударный')
#             if form_filter.cleaned_data['cat_silicon']:
#                 products_silicon = products.filter(category_id__name='Чехол силиконовый')
#         products = list(chain(products_plastic, products_shockproof, products_silicon))
#     else:
#         products = Product.objects.all()




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

    # context = {
    #     'cats': cats,
    #     'phones': phones,
    #     'products': products,
    #     'img_collection': img_collection,
    #     'phone_brands': phone_brands,
    #     'menu': menu,
    #     'title': 'Главная страница',
    #     'form_filter': form_filter,
    # }
    #
    # return render(request, 'store/index.html', context=context)


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
