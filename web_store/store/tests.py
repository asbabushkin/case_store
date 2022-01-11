"""
Great instructions from Mozilla!
https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing
"""


from django.contrib.auth import authenticate
from django.test import TestCase, Client
from django.urls import reverse

from .forms import ProductFilterForm
from .models import Product

class StoreTestCases(TestCase):

    def setUp(self):
       self.client = Client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_correct(self):
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'admin_case_store', 'password': '12345'})
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_password(self):
        user = authenticate(username='admin_case_store', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_login_wrong_username(self):
        user = authenticate(username='wrong', password='12345')
        self.assertFalse(user is not None and user.is_authenticated)


class ProductFilterFormTest(TestCase):

    def setUp(self):
        self.form = ProductFilterForm()

    def test_collection_animls_label(self):
        self.assertTrue(self.form.fields['col_animals'].label == 'Животные')

    def test_cat_plastic_label(self):
        self.assertTrue(self.form.fields['cat_plastic'].label == 'Чехлы пластиковые')

    def test_phone_name_is_hidden(self):
        self.assertTrue(self.form.fields['phone_name'].label == None)

    def test_phone_name_max_length(self):
        self.assertTrue(self.form.fields['phone_name'].max_length == 30)


# class ProductDatabaseTest(TestCase):
#
#     def setUp(self):
#        self.client = Client()
#
#     def test_products_number(self):
#         response = self.client.get(reverse('store:index'))
#         prod_list = list(response.context['products'])
#         print('prod_list: ')
#         print(prod_list)
#         print(response.context['products'])
#         self.assertTrue(len(response.context['products']) == 17)



