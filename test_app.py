import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        """Настраиваем тестовый клиент перед каждым тестом"""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        """Проверяем, что главная страница загружается"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_determinant(self):
        """Проверяем вычисление определителя"""
        response = self.app.post('/', data={'num11': '1', 'num12': '2', 'num21': '-3', 'num22': '4'})
        self.assertIn(b'10.0', response.data)

    def test_invalid_input(self):
        """Проверяем поведение при неверных данных"""
        response = self.app.post('/', data={'num11': 'one', 'num12': '2', 'num21': '-3', 'num22': '4'})
        self.assertIn("Ошибка: Ожидается число!".encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
