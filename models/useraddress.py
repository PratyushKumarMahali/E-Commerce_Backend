from typing import Optional
from pydantic import BaseModel, EmailStr

# data that api will request dor address
class UserAddress(BaseModel):
    user_id : str
    Phone_no: int
    Pincode : int
    City : str
    State : str
    Address_type : str