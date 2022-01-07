from django.test import TestCase, Client

class StoreTestCases(TestCase):
    def test_index_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_admin_login(self):
        client = Client()
        response = client.post('/admin/login/?next=/admin/', {'username': 'admin_case_store', 'password': '12345'})
        self.assertEqual(response.status_code, 200)