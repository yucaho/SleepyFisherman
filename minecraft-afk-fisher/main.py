from __future__ import annotations

from pathlib import Path

from afk_fisher.config import load_config
from afk_fisher.controller import FishingController, validate_tesseract
from afk_fisher.fisher import Fisher
from afk_fisher.ocr import OCRReader
from afk_fisher.view import ConsoleView


def main() -> None:
    root = Path(__file__).resolve().parent
    view = ConsoleView()
    view.show_startup()

    try:
        config, loaded_from_file = load_config(root)
        if not loaded_from_file:
            view.show_message("No config.json found. Copy config.example.json to config.json to customize settings.")

        OCRReader.configure_tesseract(config.tesseract_path)
        validate_tesseract()

        ocr_reader = OCRReader(config.bbox, debug_ocr=config.debug_ocr)
        fisher = Fisher(config, ocr_reader, view)
        controller = FishingController(
            fisher=fisher,
            view=view,
            start_stop_hotkey=config.start_stop_hotkey,
            exit_hotkey=config.exit_hotkey,
        )
        controller.run()

    except RuntimeError as err:
        view.show_message(str(err))
    except Exception as err:
        view.show_message(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    main()
