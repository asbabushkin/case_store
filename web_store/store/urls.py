from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('about_delivery/', about_delivery, name='about_delivery'),
    path('about_payment/', about_payment, name='about_payment'),
    path('faq/', faq, name='faq'),
    path('personal_account/', personal_account, name='personal_account'),
    path('cart/', cart, name='cart'),
    path('category/', category, name='category'),
    path('phone/', phone, name='phone'),
    path('case/<slug:product_slug>/', product_page, name='product_page'),

]