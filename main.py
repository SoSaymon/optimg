from fastapi import FastAPI, UploadFile, File, HTTPException
from starlette.middleware.cors import CORSMiddleware

from utils.get_file_type import get_file_type
from utils.ocr import perform_ocr
from utils.validate_file_size import validate_file_size

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["OPTIONS", "GET", "POST"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload(file: UploadFile = File(...), language: str = "pol"):
    allowed_file_types = ["image/jpeg", "image/png", "image/jpg"]
    file_type = get_file_type(file.file.read())

    if file_type not in allowed_file_types:
        raise HTTPException(status_code=400, detail="File type not allowed")

    max_file_size = 10 * 1024 * 1024
    validate_file_size(file.file.read(), max_file_size)

    text = await perform_ocr(file, language)
    return {"text": text}
