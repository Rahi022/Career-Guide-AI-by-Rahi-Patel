from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter(prefix="/resume")

# Ensure upload directory exists
os.makedirs("uploads", exist_ok=True)


@router.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Resume uploaded successfully"}
