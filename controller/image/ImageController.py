import base64

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, FastAPI, UploadFile,File
import os
import uuid

from starlette.responses import FileResponse

image_router = APIRouter()
image_dir = os.getenv('IMAGE_DIR')
load_dotenv()

@image_router.post("/images")
async def upload_image(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    with open(f"{image_dir}{file.filename}", "wb")as f:
        f.write(contents)

    path = f"{os.getenv('IMAGE_DIR')}{file.filename}"

    return FileResponse(path)

@image_router.get("/images")
async def get_all_images():
    image_files = [
        os.path.join(image_dir, filename)
        for filename in os.listdir(image_dir)
        if filename.endswith((".jpg", ".jpeg", ".png"))
    ]
    images_data = []
    for image_path in image_files:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            images_data.append({
                "filename": os.path.basename(image_path),
                "data": f"data:image/jpeg;base64,{encoded_string}"
            })

    return {"images": images_data}