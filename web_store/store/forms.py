from django import forms
from .models import *

class ProductFilterForm(forms.Form):
    phone_name = forms.HiddenInput()
    cat_plastic = forms.BooleanField(label='Чехлы пластиковые', required=False, initial=True)
    cat_shockproof = forms.BooleanField(label='Чехлы противоударные', required=False, initial=True)
    cat_silicon = forms.BooleanField(label='Чехлы силиконовые', required=False, initial=True)
    col_animals = forms.BooleanField(label='Животные', required=False)
    col_cartoons = forms.BooleanField(label='Мультфильмы', required=False)
    col_games = forms.BooleanField(label='Игры', required=False)
    col_anime = forms.BooleanField(label='Аниме', required=False)
    col_labels = forms.BooleanField(label='Надписи', required=False)




