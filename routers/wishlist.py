from bson import ObjectId
from models.wishlist import Wishlist
from config import database, helpers
from fastapi import APIRouter

router = APIRouter()

# add to wishlist
@router.post('/add_to_wishlist',tags=['Wishlist'])
def wishlist(request:Wishlist):
    wishlist_object =dict(request)
    wishlist_id = database.db["Wishlist"].insert_one(wishlist_object)
    return {"item added to":"wishlist"}

# wishlist list
@router.get('/wishlist_items',tags=['Wishlist'])
def find_all_items():
    return helpers.serializeList(database.db["Wishlist"].find())

# delete from cart
@router.delete('/delete_from_wishlist',tags=['Wishlist'])
def delete_from_wishlist(id):
    wishlist = database.db["Wishlist"].find_one_and_delete({"_id":ObjectId(id)})
    return {"item":"deleted"}