from typing import Union
import uvicorn
from fastapi import FastAPI
from modules import database, schemas
from datetime import datetime

app = FastAPI()

@app.post("/v1/products/create",response_model=dict)
def create_product(product: schemas.ProductCreate):
    prod = False
    inserted_variants = []
    inserted_configs = []
    db = next(database.get_db())
    try:
        prod_ = db.query(database.Product).filter_by(name=product.name).first()
        if prod_:
            raise HTTPException (status_code=400, detail="product name is already in use")
        
            vari_ = db.query(database.ProductVariant).filter_by(sku=vari.sku).first()
            if vari_:
                raise HTTPException(status_code=400, detail="product variant sku is already in use")
            inserted_variants.append(variant)
            if vari.config_attributes:
                    inserted_configs.append(config_attr)

        return {'id':prod.as_dict()['id']}
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