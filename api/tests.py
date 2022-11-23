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
    tester.test_1_create_product(valid_product)
    
    tester.test_1_create_product(valid_product,should_fail=True) # name already taken
    invalid_product = {
    
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
        "additional_info": "additional info",
        "created_at": "2020-10-23T10:37:05.085Z",
        "updated_at": "2020-10-23T10:37:05.085Z"
    
    }
    tester.test_1_create_product(invalid_product,should_fail=True) # no variants present

    valid_product = {
        "id": 1,
        "name": "Standard-hilt lightsaber 2",
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
                "sku": "EMS",
                "sales_price": 40,
                "product_id": 1,
                "purchase_price": 0,
                "type": "product",
                "created_at": "2020-10-23T10:37:05.085Z",
                "updated_at": "2020-10-23T10:37:05.085Z",
            }
        ],
        "additional_info": "additional info",
        "created_at": "2020-10-23T10:37:05.085Z",
        "updated_at": "2020-10-23T10:37:05.085Z"
    }
    
    tester.test_1_create_product(valid_product) # missing config_attributes is optional

    invalid_product = {
        "id": 1,
        "name": "Standard-hilt lightsaber 5",
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
    tester.test_1_create_product(invalid_product,should_fail=True) # variants['sku'] is not unique


    invalid_product = {
        "id": 1,
        "name": "Standard-hilt lightsaber",
        "uom": "pcs",
        "category_name": "lightsaber",
        "is_producible": True,
        "is_purchasable": True,
        "type": "something",
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
    tester.test_1_create_product(invalid_product,should_fail=True) # product 'type' must be 'product'

    invalid_product = {
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
                "type": "something_else",
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
    tester.test_1_create_product(invalid_product,should_fail=True) # variant type must be 'product'


    invalid_product = {
        "id": 1,
        "name": "Standard-hilt lightsaber 2134adr s",
        "uom": "pcs",
        "category_name": "lightsaber",
        "is_producible": True,
        "is_purchasable": True,
        "type": "product",
        "purchase_uom_conversion_rate": 1,
        "batch_tracked": False,
        "variants": [
            {
                "id": 1,
                "sku": "EM25634",
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
    tester.test_1_create_product(invalid_product,should_fail=True) # purchase_uom is required


    valid_product = {
        "id": 1,
        "name": "Standard-hilt lightsaber 891",
        "uom": "pcs",
        "category_name": "lightsaber",
        "is_producible": True,
        "is_purchasable": True,
        "type": "product",
        "purchase_uom": None,
        "purchase_uom_conversion_rate": None,
        "batch_tracked": False,
        "variants": [
            {
                "id": 1,
                "sku": "EM76",
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
    tester.test_1_create_product(valid_product) # purchase_uom can be None


    invalid_product = {
        "id": 1,
        "name": "Standard-hilt lightsaber 13 51 ",
        "uom": "pcs",
        "category_name": "lightsaber",
        "is_producible": True,
        "is_purchasable": True,
        "type": "product",
        "purchase_uom": "pcs",
        "purchase_uom_conversion_rate": None,
        "batch_tracked": False,
        "variants": [
            {
                "id": 1,
                "sku": "EM1asd",
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
    tester.test_1_create_product(invalid_product,should_fail=True) # purchase_uom_conversion_rate cant be None if purchase_uom is not None