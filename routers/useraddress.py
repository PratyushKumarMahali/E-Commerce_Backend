from bson import ObjectId
from fastapi import APIRouter
from config import database, helpers
from models.useraddress import UserAddress

router = APIRouter()

# add address
@router.post('/add_address',tags = ['UserAddress'])
def add_address(request:UserAddress):
    useraddress_object = dict(request)
    useraddress = database.db["UserAddress"].insert_one(useraddress_object)
    return {"address":"added"}

# get and update specific address information
@router.put('/address_update',tags=['UserAddress'])
def update_address(id,request:UserAddress):
    useraddress_object = dict(request)
    useraddress = database.db["UserAddress"].find_one_and_update({"_id":ObjectId(id)},{"$set":useraddress_object})
    return {"address":"updated"}

# delete specific address
@router.delete('/useraddress_delete',tags=['UserAddress'])
def delete_useraddress(id):
    useraddress = database.db["UserAddress"].find_one_and_delete({"_id":ObjectId(id)})
    return {"address":"deleted"}

# get all address information
@router.get('/all_useraddresses',tags =['UserAddress'])
def find_all_useraddresses():
    return helpers.serializeList(database.db["UserAddress"].find())