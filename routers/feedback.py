from bson import ObjectId
from config import database, helpers
from models.feedback import Feedback
from fastapi import APIRouter

router = APIRouter()

# add feedback to database
@router.post('/add_feedback',tags=['Feedback'])
def add_feedback(request:Feedback):
    feedback_object = dict(request)
    feedback_id = database.db["Feedback"].insert_one(feedback_object)
    return {"feedback":"created"}

# get single feedback information
@router.get('/feedback_search',tags=['Feedback'])
def find_feedback(id):
    return helpers.serializeDict(database.db["Feedback"].find_one({"_id":ObjectId(id)}))

# get and update specific feedback information
@router.put('/feedback_update',tags=['Feedback'])
def update_feedback(id,request:Feedback):
    feedback_object = dict(request)
    feedback = database.db["Feedback"].find_one_and_update({"_id":ObjectId(id)},{"$set":feedback_object})
    return {"feedback":"updated"}

# delete specific feedback
@router.delete('/feedback_delete',tags=['Feedback'])
def delete_poduct(id):
    feedback = database.db["Feedback"].find_one_and_delete({"_id":ObjectId(id)})
    return {"feedback":"deleted"}

# get all feedback information
@router.get('/all_feedback',tags=['Feedback'])
def find_all_feedbacks():
    return helpers.serializeList(database.db["Feedback"].find())