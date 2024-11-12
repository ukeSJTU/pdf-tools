# pdf_tools/config.py
import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Temporary directory for file processing
TEMP_DIR = BASE_DIR / "temp"
TEMP_DIR.mkdir(exist_ok=True)

# Maximum file size (in MB)
MAX_FILE_SIZE = 50

# Supported file types
SUPPORTED_EXTENSIONS = {".pdf"}
