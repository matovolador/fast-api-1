from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime, date


class ConfigAttribute(BaseModel):
    config_name : str
    config_value: str
    variant_id : int

    class Config:
        orm_mode = True

class ProductVariant(BaseModel):
    id : int
    sku: str
    sales_price: float
    product_id: int
    purchase_price: float
    type: str
    created_at: datetime
    updated_at = datetime
    product_id : int

    class Config:
        orm_mode = True
class Product(BaseModel):
    id: int
    name: str
    uom: str
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: str
    additional_info: str
    purchase_uom: Optional[str]
    purchase_uom_conversion_rate: Optional[float]
    batch_tracked: bool

    class Config:
        orm_mode = True

class VariantsCreate(ProductVariant):
    config_attributes = List[ConfigAttribute]  

class ProductCreate(Product):
    variants: List[VariantsCreate]  
