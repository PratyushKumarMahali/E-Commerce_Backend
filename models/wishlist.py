from pydantic import BaseModel

# wishlist item data
class Wishlist(BaseModel):
    product_id : str