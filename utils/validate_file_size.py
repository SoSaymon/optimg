from fastapi import HTTPException


def validate_file_size(file: bytes, file_size_limit: int):
    if len(file) > file_size_limit:
        raise HTTPException(status_code=400, detail="File size is too large")