from unittest import TestCase
from main import app
from fastapi.testclient import TestClient
from modules import database

class Tests(TestCase):
    def __init__(self):
        super().__init__()
        self.client =  TestClient(app)

    def test_1_create_product(self,product_data, should_fail=False) -> None:
