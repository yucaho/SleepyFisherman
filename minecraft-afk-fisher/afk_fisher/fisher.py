from __future__ import annotations

import threading
import time

import pyautogui

from .config import AppConfig
from .ocr import OCRReader
from .view import ConsoleView


class Fisher:
    """Core fishing loop and automation behavior."""

    def __init__(self, config: AppConfig, ocr_reader: OCRReader, view: ConsoleView) -> None:
        self.config = config
        self.ocr_reader = ocr_reader
        self.view = view
        self._fishing_active = threading.Event()

    def is_active(self) -> bool:
        return self._fishing_active.is_set()

    def start(self) -> None:
        self._fishing_active.set()

    def stop(self) -> None:
        self._fishing_active.clear()

    def right_click(self) -> None:
        pyautogui.click(button="right")

    def run(self) -> None:
        self.right_click()  # initial cast
        while self.is_active():
            text = self.ocr_reader.read_text()
            if self.config.target_text in text:
                self.view.show_bite()
                self.right_click()  # reel
                time.sleep(self.config.bite_delay_seconds)
                self.right_click()  # recast
                self.view.show_recast()
                time.sleep(self.config.recast_cooldown_seconds)
            time.sleep(self.config.scan_interval_seconds)
