from bson import ObjectId
from fastapi import APIRouter
from authentications import hashing
from config import database, helpers
from models.user import User
from routers import image

router = APIRouter()

# for user register/signup
# post is used to send data to database
@router.post('/user_register',tags =['User'])
def create_user(request:User):
   hashed_pass = hashing.Hash.bcrypt(request.password)
   profile_picture = image.profile_picture(request.image)
   user_object = dict(request)
   user_object["password"] = hashed_pass
   user_object["image"] = profile_picture
   user_id = database.db["User"].insert_one(user_object)
   return {"profile":"created"}

# get and update specific user information
@router.put('/user_update',tags=['User'])
def update_user(id,request:User):
    hashed_pass = hashing.Hash.bcrypt(request.password)
    user_object = dict(request)
    user_object["password"] = hashed_pass
    user = database.db["User"].find_one_and_update({"_id":ObjectId(id)},{"$set":user_object})
    return {"profile":"updated"}

# delete specific user
@router.delete('/user_delete',tags=['User'])
def delete_user(id):
    user = database.db["User"].find_one_and_delete({"_id":ObjectId(id)})
    return {"profile":"deleted"}

# get all user information
@router.get('/all_users',tags =['User'])
def find_all_users():
    return helpers.serializeList(database.db["User"].find())