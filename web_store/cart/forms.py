from django import forms


class CartAddProductForm(forms.Form):

    quantity = forms.IntegerField(min_value=1, max_value=20, required=False)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
