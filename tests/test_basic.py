import unittest
from base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Me aseguro que Flask se seteo correctamente
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Chequea que el indice requiera login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    # Me aseguro que welcome page cargue
    def test_welcome_route_works_as_expected(self):
        response = self.client.get('/welcome', follow_redirects=True)
        self.assertIn(b'Bienvenido a INSPT-TP Final', response.data)

    # Chequea que aparezca el menu en la main page
    def test_menu_show_up_on_main_page(self):
        response = self.client.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'item de test', response.data)


if __name__ == '__main__':
    unittest.main()