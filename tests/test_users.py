import unittest
from passlib.hash import sha256_crypt
from flask import request
from flask.ext.login import current_user
from base import BaseTestCase
from project.models import User


class TestUser(BaseTestCase):

    # Chequea que el usuario pueda registrarse
    def test_user_registration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                username='Michael', email='michael@realpython.com',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Bienvenido a INSPT-TP Final', response.data)
            self.assertTrue(current_user.username == "Michael")
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='michael@realpython.com').first()
            self.assertTrue(str(user) == '<username: Michael, email: michael@realpython.com')

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                username='Michael', email='michael',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)
            self.assertIn('/register', request.url)

    # Ensure id is correct for the current/logged in user
    def test_get_by_id(self):    
        with self.client:
            self.client.post('/login', data=dict(
                username="admin", password='admin'
            ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)

    # Ensure given password is correct after unhashing
    def test_check_password(self):        
        user = User.query.filter_by(email='ad@min.com').first()
        self.assertTrue(sha256_crypt.verify('admin', user.password))
        self.assertFalse(sha256_crypt.verify('foobar', user.password))


class UserViewsTest(BaseTestCase):

    # Me aseguro que la pagina de login cargue correctamente
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Por favor hace login' in response.data)

    # Chequea que el login se comporte correctamente con credenciales correctas
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
            )
            self.assertIn(b'Acabas de loguearte!', response.data)
            self.assertTrue(current_user.username == 'admin')
            self.assertTrue(current_user.is_active())

    # Chequea que el login se comporte correctamente con credenciales invalidas
    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username='mal', password='mal'),
            follow_redirects=True
        )
        self.assertIn(b'Credenciales invalidas. Proba de nuevo', response.data)

    # Chequea que el logout se comporte correctamente
    def test_logout(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'Acabas de desloguearte!', response.data)
            self.assertFalse(current_user.is_active())

    # Chequea que el logout requiera login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)


if __name__ == '__main__':
    unittest.main()