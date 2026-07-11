from datetime import datetime 
from pydantic import BaseModel 

class Product(BaseModel):
    title:str
    price:float
    currency:str
    url:str


class ProductSnapshot(BaseModel):
    product:Product 
    timestamp:datetime

class ScrapeResult(BaseModel):
    products:list[Product]
    source:str

    