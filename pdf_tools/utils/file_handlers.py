# pdf_tools/utils/file_handlers.py
import io
from typing import Union
from pathlib import Path
import base64


class FileHandler:
    @staticmethod
    def create_download_link(file_bytes: bytes, filename: str) -> str:
        b64 = base64.b64encode(file_bytes).decode()
        return f'<a href="data:application/pdf;base64,{b64}" download="{filename}">点击下载处理后的文件</a>'
