from typing import Union
import uvicorn
from fastapi import FastAPI
from modules import database, schemas
from datetime import datetime

app = FastAPI()

@app.post("/v1/products/create")
def create_product(product: schemas.ProductCreate):
    db = next(database.get_db())
    prod = database.Product(
        name = product.name,
        uom = product.uom,
        category_name = product.category_name,
        is_producible = product.is_producible,
        is_purchasable = product.is_purchasable,
        type = 'product',
        additional_info = product.additional_info,
        purchase_uom = product.purchase_uom,
        purchase_uom_conversion_rate = product.purchase_uom_conversion_rate,
        batch_tracked = product.batch_tracked,
        created_at = datetime.now(),
        updated_at = datetime.now()
    )
    db.add(prod)
    db.commit()
    db.refresh(prod)

    for vari in product.variants:
        variant = database.ProductVariant(
            sku = vari.sku,
            sales_price = vari.sales_price,
            product_id = prod.id,
            type = 'product',
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        db.add(variant)
        db.commit()
        db.refresh(variant)

        for config in vari.config_attributes:
            config_attr = database.ConfigAttribute(
                config_name = config.config_name,
                config_value = config.config_value,
                variant_id = variant.id 
            )
            db.add(config_attr)

    
    db.commit()
    db.refresh(product)
    db.close()
    return product


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)