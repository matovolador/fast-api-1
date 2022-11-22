[![Coverage Status](./api/coverage/coverage-badge.svg?dummy=8484744)](./backend/coverage/coverage.xml)

## Unbridaled Python Interview

We want like you to create a single endpoint following the following spec using FastAPI. Your FastAPI project should contain the following

* model (needs to be able to read and write data to `postgres`)
* migration
* handler

### Create an endpoint 

Create an endpoint with route: `POST /v1/products/create` that takes in the following request payload.

```json
{
    "id": 1,
    "name": "Standard-hilt lightsaber",
    "uom": "pcs",
    "category_name": "lightsaber",
    "is_producible": true,
    "is_purchasable": true,
    "type": "product",
    "purchase_uom": "pcs",
    "purchase_uom_conversion_rate": 1,
    "batch_tracked": false,
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
```

Here are the explanations on each of the tables. A `Product` has many `ProductVariants`. You will be free to determine the best DB type for each column. Make sure you do foreign key and make any design considerations like you would designing a production ERP/ecommerce system. 

The endpoint should create the product and variants ALL in a single transaction and rollback if necessary. You will be expected to write validations in the request body parsing layer (using marshmallow or pydantic). 

### Product Object 

|    Attribute    |    Description    |
|    ---    |    ---    |
| id | Unique identifier for the object. |
| name | The product's unique name. |
|    uom    | The unit used to measure the quantity of the product (e.g. pcs, kg, m). This unit is also used for the item on orders and product recipes.    |
|    category_name    |    A string used to group similar items for better organization and analysis.   |
|    is_producible    |    If you make the product, this enables creating product recipes and production operations for the product and adding it to manufacturing orders. |
|    is_purchasable    |    If you purchase the product from suppliers and sell directly to your customers without any production process, you can make a product purchasable. |
|    type    |    Indicating the item type. Product objects are of type `product`. |
|    additional_info    |    A string attached to the object to add any internal comments, links to external files, additional instructions, etc.    |
|    purchase_uom    |    If you are purchasing in a different unit of measure than the default unit of measure (used for tracking stock) for this item, you can define the purchase unit. Value *null* indicates that purchasing is done in same unit of measure. If value is not *null*, purchase_uom_conversion_rate must also be populated. |
| purchase_uom_conversion_rate |    The conversion rate between the purchase and product UoMs. If used, product must have a purchase_uom that is different from uom.    |
|    batch_tracked    |    Batch tracking enables you to assign batch numbers and expiration dates to manufactured items.    |
|    variants    |    An array of product variant objects.    |
|    created_at    |    The timestamp when the product was created.    |
|    updated_at    |    The timestamp when the product was last updated.    |


### ProductVariant Object

```json
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
```
   
|    Attribute    |    Description    |
|    ---    |    ---    |
|    id    |    Unique identifier for the object.    |
|    sku    |    Unique per sku    |
|    sales_price    |   Sales price of the variant  |
|    purchase_price    |  Purchase price of the variant |
|    config_attributes | Array of dictionaries |

### Testing 

Write a simple test that tests your endpoint functionality using your favourite python testsuite (pytest, unittest, etc.).

### Deployment (Bonus)

If time permits, deploy the FastAPI API on Heroku (use free dyno). 



