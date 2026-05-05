from __future__ import annotations

from typing import Tuple

import pytesseract
from PIL import ImageGrab


class OCRReader:
    def __init__(self, bbox: Tuple[int, int, int, int], debug_ocr: bool = False) -> None:
        self.bbox = bbox
        self.debug_ocr = debug_ocr

    @staticmethod
    def configure_tesseract(tesseract_path: str) -> None:
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path

    @staticmethod
    def verify_tesseract() -> None:
        pytesseract.get_tesseract_version()

    def read_text(self) -> str:
        screenshot = ImageGrab.grab(bbox=self.bbox)
        text = pytesseract.image_to_string(screenshot)
        cleaned = text.strip()
        if self.debug_ocr and cleaned:
            print(f"[OCR] {cleaned}")
        return cleaned
