from bson import ObjectId
from models.cart import Cart
from config import database, helpers
from fastapi import APIRouter

router = APIRouter()

# add to cart
@router.post('/add_to_cart',tags=['Cart'])
def cart(request:Cart):
    cart_object =dict(request)
    cart_id = database.db["Cart"].insert_one(cart_object)
    return {"item added to":"cart"}

# cart list
@router.get('/cart_items',tags=['Cart'])
def find_all_items():
    return helpers.serializeList(database.db["Cart"].find())

# update cart
@router.put('/update_cart',tags=['Cart'])
def update_cart(id,request:Cart):
    cart_object = dict(request)
    cart_id = database.db["Cart"].find_one_and_update({"_id":ObjectId(id)},{"$set":cart_object})
    return {"cart":"updated"}

# delete from cart
@router.delete('/delete_cart',tags=['Cart'])
def delete_cart(id):
    product = database.db["Cart"].find_one_and_delete({"_id":ObjectId(id)})
    return {"item":"deleted"}