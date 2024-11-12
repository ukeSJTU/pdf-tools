# pdf_tools/core/pdf_analyzer.py
import pdfplumber
from typing import Union, Dict, Any
from pathlib import Path
import io


class PDFAnalyzer:
    @staticmethod
    def get_pdf_info(pdf_file: Union[Path, io.BytesIO]) -> Dict[str, Any]:
        with pdfplumber.open(pdf_file) as pdf:
            first_page = pdf.pages[0]
            return {
                "页数": len(pdf.pages),
                "页面大小": f"{first_page.width:.2f} x {first_page.height:.2f} 点",
                "文档信息": pdf.metadata,
            }
