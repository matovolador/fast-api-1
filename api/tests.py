from unittest import TestCase
from main import app
from fastapi.testclient import TestClient
from modules import database

class Tests(TestCase):
    def __init__(self):
        super().__init__()
        self.client =  TestClient(app)

    def test_1_create_product(self) -> None:
        valid_product = {
            "id": 1,
            "name": "Standard-hilt lightsaber",
            "uom": "pcs",
            "category_name": "lightsaber",
            "is_producible": True,
            "is_purchasable": True,
            "type": "product",
            "purchase_uom": "pcs",
            "purchase_uom_conversion_rate": 1,
            "batch_tracked": False,
            "variants": [
                {
                    "id": 1,
                    "sku": "EM",
                    "sales_price": 40,
                    "product_id": 1,
                    "purchase_price": 0,
                    "type": "product",
                    "created_at": "2020-10-23T10:37:05.085Z",
                    "updated_at": "2020-10-23T10:37:05.085Z",
                    "config_attributes": [
                        {
                            "config_name": "Type",
                            "config_value": "Standard"
                        }
                    ]
                }
            ],
            "additional_info": "additional info",
            "created_at": "2020-10-23T10:37:05.085Z",
            "updated_at": "2020-10-23T10:37:05.085Z"
        }
        response = self.client.post('/v1/products/create', json=valid_product)
        print(response.text)
        self.assertEqual(200, response.status_code)
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
    tester.test_1_create_product()