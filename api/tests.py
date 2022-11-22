from unittest import TestCase, mock
from main import app
from fastapi.testclient import TestClient


class TestIntegrationMain(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    @mock.patch('main.books', [])
    def test_integration_givenValidBook_whenCreateBook_thenReturnCreatedBook(self) -> None:
        valid_book = {
            'isbn': 9780132350884,
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship'
        }
        response = self.client.post('/books/', json=valid_book)

        self.assertEqual(200, response.status_code)
        self.assertEqual(valid_book, response.json())