from pydantic import BaseModel
from typing import Optional

# product data
class Product(BaseModel):
    product_name : str
    product_photo : str
    product_category : str
    product_description : str
    product_price : float
    product_count : int
    product_discount : float
    rating : Optional[int]