from fastapi import APIRouter, UploadFile, File
from typing import List
from typing import List
import shutil
import os

from src.models.predict import predict_multiple

router = APIRouter()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.get("/")
def home():
    return {"message": "Skin Disease API Running"}


@router.post("/predict")
def predict_api(files: List[UploadFile] = File(...)):
    file_paths = []
    
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_paths.append(file_path)

    label, confidence = predict_multiple(file_paths)

    return {
        "prediction": label,
        "confidence": round(confidence * 100, 2),
        "num_files": len(file_paths)
    }