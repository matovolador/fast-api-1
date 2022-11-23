from unittest import TestCase
from main import app
from fastapi.testclient import TestClient
from modules import database

class Tests(TestCase):
    def __init__(self):
        super().__init__()
        self.client =  TestClient(app)

    def test_1_create_product(self,product_data, should_fail=False) -> None:
        response = self.client.post('/v1/products/create', json=product_data)
        print(response.text)
        if not should_fail:
            self.assertEqual(200, response.status_code)
        else:
            self.assertNotEqual(200,response.status_code)
        print(response.json())
        print("test 1 completed")

if __name__ == "__main__":
    # clean db
    db = next(database.get_db())
    db.query(database.ConfigAttribute).delete()
    db.query(database.ProductVariant).delete()
    db.query(database.Product).delete()
    db.commit()
    db.close()
    # -- 
    tester = Tests()
