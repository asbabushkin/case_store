from django import forms
from .models import *

class ProductFilterForm(forms.Form):

    cat_plastic = forms.BooleanField(label='Чехлы пластиковые', required=False)
    cat_shockproof = forms.BooleanField(label='Чехлы противоударные', required=False)
    cat_silicon = forms.BooleanField(label='Чехлы силиконовые', required=False)


    min_price = forms.IntegerField(label='Цена от ', required=False)
    max_price = forms.IntegerField(label='Цена до', required=False)



