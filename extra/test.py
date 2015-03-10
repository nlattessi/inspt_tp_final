import unittest
from tests.base import BaseTestCase


class MenuCategoriaPostTests(BaseTestCase):

    # Me aseguro que un usuario logueado pueda agregar una nueva categoria
    def test_user_can_post(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.post(
                '/',
                data=dict(nombre="test"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Una nueva categoria ha sido agregada.',
                          response.data)


if __name__ == '__main__':
    unittest.main()