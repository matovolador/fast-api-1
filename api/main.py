from typing import Union
import uvicorn
from fastapi import FastAPI, HTTPException
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

        
        for vari in product.variants:
            vari_ = db.query(database.ProductVariant).filter_by(sku=vari.sku).first()
            if vari_:
                raise HTTPException(status_code=400, detail="product variant sku is already in use")
            
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
            inserted_variants.append(variant)
            
            if vari.config_attributes:
                for config in vari.config_attributes:
                    config_attr = database.ConfigAttribute(
                        config_name = config.config_name,
                        config_value = config.config_value,
                        variant_id = variant.id 
                    )
                    db.add(config_attr)
                    db.commit()
                    inserted_configs.append(config_attr)

        
        db.commit()
        db.refresh(prod)
        db.close()
        return {'id':prod.as_dict()['id']}
    except Exception as e:
        for entry in inserted_configs:
            db.delete(entry)
        for entry in inserted_variants:
            db.delete(entry)
        if prod:
            db.delete(prod)
        db.commit()
        db.close()
        raise HTTPException(status_code=400,detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)