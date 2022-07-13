from pydantic import BaseModel, EmailStr
from typing import Optional

# login data for user
class Login(BaseModel):
    username : EmailStr
    password : str

# token format
class Token(BaseModel):
    access_token : str
    token_type : str

# token data format
class TokenData(BaseModel):
    email : Optional[EmailStr] = None