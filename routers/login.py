from authentications import hashing
from authentications import JWTtoken
from config import database
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

# for user login
# post is used to send request to database to verify the credentials
@router.post('/user_login',tags=['Login'])
def user_login(request:OAuth2PasswordRequestForm = Depends()):
	user = database.db["User"].find_one({"email":request.username})
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.username} username')
	if not hashing.Hash.verify(user["password"], request.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
	access_token = JWTtoken.create_access_token(data={"sub": user["username"]})
	return {"access_token": access_token, "token_type": "bearer"}