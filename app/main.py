from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

from app.storage import (
    save_file,
    list_files,
    get_file,
    delete_file,
)

app = FastAPI(
    title="Simple Picture Upload API",
    version="1.0.0",
    description="A tiny API for uploading and retrieving pictures."
)

ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
    "image/gif",
}


@app.get("/")
def root():
    return {
        "message": "Picture Upload API",
        "docs": "/docs",
    }


@app.post("/upload")
async def upload_picture(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed."
        )

    filename = save_file(file)

    return {
        "message": "Upload successful",
        "filename": filename,
    }


@app.get("/images")
def get_images():
    return {
        "count": len(list_files()),
        "images": list_files(),
    }


@app.get("/images/{filename}")
def download_image(filename: str):
    file = get_file(filename)

    if not file:
        raise HTTPException(
            status_code=404,
            detail="Image not found."
        )

    return FileResponse(file)


@app.delete("/images/{filename}")
def remove_image(filename: str):
    deleted = delete_file(filename)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Image not found."
        )

    return {"message": "Deleted"}
