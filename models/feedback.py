from pydantic import BaseModel

# feedback access
class Feedback(BaseModel):
    username : str
    product_name : str
    rating: int
    comment: str