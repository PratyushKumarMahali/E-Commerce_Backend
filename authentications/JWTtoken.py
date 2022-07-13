from datetime import datetime, timedelta
from jose import JWTError, jwt
from models import login

SECRET_KEY = "372df48b32741d7b6b7a424934a3ad75cd98dc00f2d305030ca81a4fd70fe3c6"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# create the access token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# verify the access token
def verify_token(token:str,credentials_exception):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		email: str = payload.get("sub")
		if email is None:
			raise credentials_exception
		token_data = login.TokenData(email = email)
	except JWTError:
	    raise credentials_exception