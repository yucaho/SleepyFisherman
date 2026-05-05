from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


@dataclass(slots=True)
class AppConfig:
    tesseract_path: str
    bbox: Tuple[int, int, int, int]
    target_text: str
    scan_interval_seconds: float
    bite_delay_seconds: float
    recast_cooldown_seconds: float
    start_stop_hotkey: str
    exit_hotkey: str
    debug_ocr: bool = False


DEFAULT_CONFIG = AppConfig(
    tesseract_path="",
    bbox=(1820, 530, 2460, 1220),
    target_text="Fishing Bobber splash",
    scan_interval_seconds=0.2,
    bite_delay_seconds=0.5,
    recast_cooldown_seconds=1.8,
    start_stop_hotkey="f6",
    exit_hotkey="f7",
    debug_ocr=False,
)


def load_config(root: Path) -> tuple[AppConfig, bool]:
    config_path = root / "config.json"
    if not config_path.exists():
        return DEFAULT_CONFIG, False

    with config_path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)

    bbox_values = tuple(raw.get("bbox", list(DEFAULT_CONFIG.bbox)))
    if len(bbox_values) != 4:
        raise ValueError("Config value 'bbox' must contain exactly four integers.")

    return AppConfig(
        tesseract_path=raw.get("tesseract_path", DEFAULT_CONFIG.tesseract_path),
        bbox=tuple(int(v) for v in bbox_values),
        target_text=raw.get("target_text", DEFAULT_CONFIG.target_text),
        scan_interval_seconds=float(raw.get("scan_interval_seconds", DEFAULT_CONFIG.scan_interval_seconds)),
        bite_delay_seconds=float(raw.get("bite_delay_seconds", DEFAULT_CONFIG.bite_delay_seconds)),
        recast_cooldown_seconds=float(raw.get("recast_cooldown_seconds", DEFAULT_CONFIG.recast_cooldown_seconds)),
        start_stop_hotkey=raw.get("start_stop_hotkey", DEFAULT_CONFIG.start_stop_hotkey),
        exit_hotkey=raw.get("exit_hotkey", DEFAULT_CONFIG.exit_hotkey),
        debug_ocr=bool(raw.get("debug_ocr", DEFAULT_CONFIG.debug_ocr)),
    ), True
