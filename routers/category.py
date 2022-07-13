from bson import ObjectId
from config import database, helpers
from models.category import Category
from fastapi import APIRouter

router = APIRouter()

# add category to database
@router.post('/add_category',tags=['Category'])
def add_category(request:Category):
    category_object = dict(request)
    category_id = database.db["Category"].insert_one(category_object)
    return {"category":"created"}

# get single category information
@router.get('/category_search',tags=['Category'])
def find_category(category_name):
    return helpers.serializeDict(database.db["Category"].find_one({"category_name":category_name}))

# get and update specific category information
@router.put('/category_update',tags=['Category'])
def update_category(id,request:Category):
    category_object = dict(request)
    category = database.db["Category"].find_one_and_update({"_id":ObjectId(id)},{"$set":category_object})
    return {"category":"updated"}

# delete specific category
@router.delete('/category_delete',tags=['Category'])
def delete_category(id):
    category = database.db["Category"].find_one_and_delete({"_id":ObjectId(id)})
    return {"category":"deleted"}

# get all category information
@router.get('/all_category',tags=['Category'])
def find_all_category():
    return helpers.serializeList(database.db["Category"].find())