from pydantic import BaseModel, root_validator, validator
from typing import Optional,List
from datetime import datetime, date


class ConfigAttribute(BaseModel):
    config_name : str
    config_value: str

    

class ProductVariant(BaseModel):
    id : int
    sku: str
    sales_price: float
    product_id: int
    purchase_price: float
    type: str
    created_at: str
    updated_at = str

    @validator('type')
    def variant_type(cls, v):
        if v != 'product':
            raise ValueError('invalid product type')
        return v

class Product(BaseModel):
    id: int
    name: str
    uom: str
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: str
    additional_info: str
    purchase_uom: Optional[str] = ...
    purchase_uom_conversion_rate: Optional[float] = ...
    batch_tracked: bool
    created_at : str
    updated_at : str

    @root_validator
    def conversion_rate_not_none_if_purchase_uom_is_none(cls, values):
        p_uom, c_rate = values.get('purchase_uom'), values.get('purchase_uom_conversion_rate')
        if p_uom is not None and c_rate is None:
            raise ValueError('purchase_uom_conversion_rate must be populated if purchase_uom is not null')
        return values

    @validator('type')
    def product_type(cls, v):
        if v != 'product':
            raise ValueError('invalid product type')
        return v


class VariantCreate(ProductVariant):
    config_attributes : Optional[List[ConfigAttribute]]


class ProductCreate(Product):
    variants: List[VariantCreate]  

