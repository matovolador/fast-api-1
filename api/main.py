from typing import Union
import uvicorn
from fastapi import FastAPI
from modules import database, schemas

app = FastAPI()

@app.post("/v1/products/create",response_model=schemas.Product)
def create_product(db: database.Session, product: schemas.ProductCreate):
    product = database.Product(
        name = product.name,
        uom = product.uom,
        category_name = product.category_name,
        is_producible = product.is_producible,
        type = 'product',
        additional_info = product.additional_info,
        purchase_uom = product.purchase_uom,
        purchase_uom_conversion_rate = product.purchase_uom_conversion_rate,
        batch_tracked = product.batch_tracked,
        created = datetime.now(),
        updated_at = datetime.now()
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    for vari in product.variants:
        variant = database.ProductVariants(
            id = vari.id
        )
        db.add(variant)
    product = database.Product(
        name = product.name
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    return product


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)