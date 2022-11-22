from unittest import TestCase, mock
from main import app
from fastapi.testclient import TestClient


class TestIntegrationMain(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    @mock.patch('main.products', [])
    def test_create_product(self) -> None:
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

        self.assertEqual(200, response.status_code)
        self.assertEqual(valid_product, response.json())