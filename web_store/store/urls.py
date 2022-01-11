from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', StoreHome.as_view(), name='index'),
    path('product/<slug:product_slug>', ProductPage.as_view(), name='product_page'),
    path('cart/', CartPage.as_view(), name='cart'),
    path('about/', about, name='about'),
    path('about_delivery/', about_delivery, name='about_delivery'),
    path('about_payment/', about_payment, name='about_payment'),
    path('faq/', faq, name='faq'),
    path('personal_account/', personal_account, name='personal_account'),
    path('category/', category, name='category'),
    path('phone/', phone, name='phone'),
    path('login/', login, name='login'),


]