from django.urls import path
from .views import *


app_name = 'store'
urlpatterns = [
    path('', StoreHome.as_view(), name='index'),
    path('product/<slug:product_slug>', ProductPage.as_view(), name='product_page'),
    path('about_delivery/', about_delivery, name='about_delivery'),
    path('about_payment/', about_payment, name='about_payment'),
    path('faq/', faq, name='faq'),
]