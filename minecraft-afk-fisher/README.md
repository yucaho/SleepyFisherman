# Minecraft AFK Fisher (Educational)

A lightweight, portfolio-ready Python project that demonstrates a clean project structure, thread-safe hotkey control, OCR integration with Tesseract, and simple automation workflow design.

## Disclaimer

This project is for **educational and personal-use experimentation only**. Automation may violate Minecraft server rules, anti-cheat policies, or terms of service. Only use this in environments where automation is explicitly allowed (for example, personal/local test worlds).

## Features

- Light MVC-style organization (`fisher`, `ocr`, `view`, `controller` modules).
- Thread-safe start/stop behavior using `threading.Event` and a lock.
- OCR text detection from a configurable screen region using `pytesseract`.
- Configurable timing, keys, and target text with `config.json`.
- Friendly console messages and beginner-friendly code layout.

## Requirements

- Python 3.10+
- Tesseract OCR installed
- Minecraft subtitles/captions enabled (for text detection)

Python packages:

- `pyautogui`
- `pytesseract`
- `pillow`
- `keyboard`

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy config template:

```bash
cp config.example.json config.json
```

5. Edit `config.json` for your machine and screen region.

## Tesseract on Windows

If Tesseract is not in your system `PATH`, set `tesseract_path` in `config.json` to the full executable path (example below):

```json
"tesseract_path": "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```

## Configuration

`config.py` loads `config.json` when present. If missing, defaults are used and the app will tell you to copy `config.example.json`.

Config values:

- `tesseract_path`
- `bbox` (`[left, top, right, bottom]`)
- `target_text`
- `scan_interval_seconds`
- `bite_delay_seconds`
- `recast_cooldown_seconds`
- `start_stop_hotkey`
- `exit_hotkey`
- `debug_ocr`

## Run

```bash
python main.py
```

## Hotkeys

- `F6` (default): Start/stop fishing
- `F7` (default): Exit script cleanly

## Troubleshooting

### Tesseract not found

- Confirm Tesseract is installed.
- If needed, set `tesseract_path` in `config.json`.
- Verify executable path is correct.

### OCR not detecting text

- Turn on `debug_ocr` in `config.json`.
- Ensure Minecraft subtitles are enabled.
- Confirm `target_text` matches your language/client text.

### Wrong screen region

- Update `bbox` values in `config.json` so the subtitle area is captured.
- Test with smaller regions first.

### Fullscreen capture issues

- Some systems block capture in exclusive fullscreen.
- Switch Minecraft to borderless/windowed mode and retry.

## Future Improvements

- GUI calibration helper for subtitle region.
- Click-and-drag region selector tool.
- Optional `mss` screenshot backend for speed.
- Packaged `.exe` release for easier usage.
- Structured logging to file.
