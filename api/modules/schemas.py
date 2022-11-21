from pydantic import BaseModel

class Product(BaseModel):
    name: str
    class Config:
        orm_mode = True
