from typing import Optional
from pydantic import BaseModel, EmailStr

# data that api will request for user registration
class User(BaseModel):
    username : str
    image : str
    email : EmailStr
    password : str