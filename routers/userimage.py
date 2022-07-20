import uuid
import aiofiles
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

# upload profile picture
@router.post("/profile_picture",tags=['ProfilePicture'])
async def profile_picture(profile_picture:UploadFile=File(...)):
    file_name = uuid.uuid4()
    async with aiofiles.open(f"user/{file_name}.jpg","wb") as out_file:
        while content := await profile_picture.read(1024):
            await out_file.write(content)
    return {"image":"uploaded"}