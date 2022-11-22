from typing import Union
import uvicorn
from fastapi import FastAPI
from modules import database, schemas

app = FastAPI()

@app.post("/v1/products/create",response_model=schemas.Product)
def create_product(db: database.Session, product: schemas.ProductCreate):
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