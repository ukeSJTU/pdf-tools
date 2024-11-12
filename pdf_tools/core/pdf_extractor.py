# pdf_tools/core/pdf_extractor.py
import pdfplumber
from typing import Union
from pathlib import Path
import io


class PDFExtractor:
    @staticmethod
    def extract_text(pdf_file: Union[Path, io.BytesIO]) -> str:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
                text += "\n\n"
            return text
