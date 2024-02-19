from fastapi import FastAPI, UploadFile, File, HTTPException
from starlette.middleware.cors import CORSMiddleware

from utils.get_file_type import get_file_type
from utils.ocr import perform_ocr
from utils.save_files import scramble_filename, save_file

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
    filename = scramble_filename(file.filename)
    await save_file(file, filename)
    text = await perform_ocr(f"files/{file.filename}", language)
    return {"filename": filename, "text": text}
