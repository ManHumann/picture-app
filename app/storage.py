from pathlib import Path
import shutil
import uuid

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_file(upload_file):
    extension = Path(upload_file.filename).suffix.lower()
    filename = f"{uuid.uuid4()}{extension}"

    destination = UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return filename


def list_files():
    return sorted(
        [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()]
    )


def get_file(filename):
    path = UPLOAD_DIR / filename
    if path.exists():
        return path
    return None


def delete_file(filename):
    path = UPLOAD_DIR / filename
    if path.exists():
        path.unlink()
        return True
    return False
