# pdf_tools/utils/validators.py
from pathlib import Path
from typing import Union
import io
from ..config import MAX_FILE_SIZE, SUPPORTED_EXTENSIONS


class FileValidator:
    @staticmethod
    def validate_file(file: Union[Path, io.BytesIO]) -> bool:
        if isinstance(file, io.BytesIO):
            # Check file size for BytesIO
            file_size = len(file.getvalue()) / (1024 * 1024)  # Convert to MB
            return file_size <= MAX_FILE_SIZE

        # Check file extension and size for Path
        return (
            file.suffix.lower() in SUPPORTED_EXTENSIONS
            and (file.stat().st_size / (1024 * 1024)) <= MAX_FILE_SIZE
        )
