from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Me aseguro que Flask se seteo correctamente
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Me aseguro que la pagina de login cargue correctamente
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Por favor hace login' in response.data)

    # Chequea que el login se comporte correctamente con credenciales correctas
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'Acabas de loguearte!', response.data)

    # Chequea que el login se comporte correctamente con credenciales invalidas
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='mal', password='mal'),
            follow_redirects=True
        )
        self.assertIn(b'Credenciales invalidas. Proba de nuevo', response.data)

    # Chequea que el logout se comporte correctamente
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'Acabas de desloguearte!', response.data)

    # Chequea que el indice requiera login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'Tenes que loeguarte primero.' in response.data)

    # Chequea que aparezca el menu en la main page
    def test_menu_show_up(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'hamburgesa con queso', response.data)

if __name__ == '__main__':
    unittest.main()