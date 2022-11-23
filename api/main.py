from typing import Union
import uvicorn
from fastapi import FastAPI
from modules import database, schemas
from datetime import datetime

app = FastAPI()

@app.post("/v1/products/create")
def create_product(product: schemas.ProductCreate):
    prod = False
    inserted_variants = []
    inserted_configs = []
    db = next(database.get_db())
            inserted_variants.append(variant)
                    inserted_configs.append(config_attr)

        for entry in inserted_configs:
            db.delete(entry)
        for entry in inserted_variants:
            db.delete(entry)
        if prod:
            db.delete(prod)
        db.commit()
        db.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)