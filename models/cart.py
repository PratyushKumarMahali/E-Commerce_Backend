from pydantic import BaseModel

# cart item data
class Cart(BaseModel):
    product_id : str
    quantity : int