from __future__ import annotations

import threading
from typing import Optional

import keyboard
import pytesseract

from .fisher import Fisher
from .view import ConsoleView


class FishingController:
    """Handles keyboard input and thread lifecycle management."""

    def __init__(self, fisher: Fisher, view: ConsoleView, start_stop_hotkey: str, exit_hotkey: str) -> None:
        self.fisher = fisher
        self.view = view
        self.start_stop_hotkey = start_stop_hotkey
        self.exit_hotkey = exit_hotkey
        self._thread_lock = threading.Lock()
        self._fishing_thread: Optional[threading.Thread] = None
        self._shutdown_event = threading.Event()

    def toggle_fishing(self) -> None:
        with self._thread_lock:
            if self.fisher.is_active():
                self.fisher.stop()
                self.view.show_stop()
                return

            if self._fishing_thread and self._fishing_thread.is_alive():
                return

            self.fisher.start()
            self._fishing_thread = threading.Thread(target=self.fisher.run, name="fishing-thread", daemon=True)
            self._fishing_thread.start()
            self.view.show_start()

    def shutdown(self) -> None:
        self.fisher.stop()
        with self._thread_lock:
            if self._fishing_thread and self._fishing_thread.is_alive():
                self._fishing_thread.join(timeout=5)
        self.view.show_exit()

    def request_exit(self) -> None:
        self._shutdown_event.set()

    def run(self) -> None:
        keyboard.add_hotkey(self.start_stop_hotkey, self.toggle_fishing)
        keyboard.add_hotkey(self.exit_hotkey, self.request_exit)
        self.view.show_message(
            f"Press {self.start_stop_hotkey.upper()} to start/stop fishing. "
            f"Press {self.exit_hotkey.upper()} to exit."
        )
        self._shutdown_event.wait()
        self.shutdown()


def validate_tesseract() -> None:
    try:
        pytesseract.get_tesseract_version()
    except pytesseract.pytesseract.TesseractNotFoundError as exc:
        raise RuntimeError(
            "Tesseract not found. Set 'tesseract_path' in config.json to your tesseract.exe path "
            "or install Tesseract and add it to PATH."
        ) from exc
