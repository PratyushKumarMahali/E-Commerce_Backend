from bson import ObjectId
from config import database, helpers
from models.product import Product
from fastapi import APIRouter

router = APIRouter()

# add product to database
@router.post('/add_product',tags=['Product'])
def add_product(request:Product):
    product_object = dict(request)
    product_id = database.db["Product"].insert_one(product_object)
    return {"product":"created"}

# get single product information
@router.get('/product_search',tags=['Product'])
def find_product(product_name):
    return helpers.serializeList(database.db["Product"].find({'product_name':{'$regex':product_name}},{'product_name':1,'created_at':1}))

# get and update specific product information
@router.put('/product_update',tags=['Product'])
def update_product(id,request:Product):
    product_object = dict(request)
    product = database.db["Product"].find_one_and_update({"_id":ObjectId(id)},{"$set":product_object})
    return {"product":"updated"}

# delete specific product
@router.delete('/product_delete',tags=['Product'])
def delete_poduct(id):
    product = database.db["Product"].find_one_and_delete({"_id":ObjectId(id)})
    return {"product":"deleted"}

# get all product information
@router.get('/all_product',tags=['Product'])
def find_all_products():
    return helpers.serializeList(database.db["Product"].find())