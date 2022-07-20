import uuid
import aiofiles
from typing import List
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

# upload product image
@router.post("/product_image",tags=['ProductImages'])
async def product_images(product_images:List[UploadFile]=File(...)):
    for file in product_images:
        file_name = uuid.uuid4()
        async with aiofiles.open(f"product/{file_name}.jpg","wb") as out_file:
            while content := await file.read(1024):
                await out_file.write(content)
    return {"image":"uploaded"}