from typing import Union
import uvicorn
from fastapi import FastAPI
from modules import database, schemas

app = FastAPI()

@app.post("/v1/products/create")
def create_product(product:schemas.Product):



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)