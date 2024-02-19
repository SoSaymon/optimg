import uuid


def scramble_filename(filename: str) -> str:
    return f"{uuid.uuid4()}.{filename.split('.')[-1]}"


async def save_file(file, filename: str) -> str:
    file_path = f"files/{filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return file_path
