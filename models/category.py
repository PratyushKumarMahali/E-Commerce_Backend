from pydantic import BaseModel

#category data
class Category(BaseModel):
    category_name : str
    category_description : str
    is_category_active : bool