# pdf_tools/core/pdf_merger.py
from pathlib import Path
import PyPDF2
from typing import List, Union
import io


class PDFMerger:
    @staticmethod
    def merge_pdfs(pdf_files: List[Union[Path, io.BytesIO]]) -> bytes:
        merger = PyPDF2.PdfMerger()

        try:
            for pdf in pdf_files:
                merger.append(pdf)

            output = io.BytesIO()
            merger.write(output)
            return output.getvalue()
        finally:
            merger.close()
