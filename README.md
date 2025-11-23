# Clipboard Copilot

Local-first clipboard automation that watches for changes and applies context-aware actions entirely offline.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Typical Actions](#typical-actions)
- [Architecture](#architecture)
- [Plugins](#plugins)
- [Development](#development)
- [Roadmap](#roadmap)
- [Privacy](#privacy)

## Overview
Clipboard Copilot turns everyday copy/paste into a productivity flow. It detects the content type of your clipboard and applies the most relevant action (e.g., convert CSV to JSON, clean Markdown formatting) fully locally.

## Features
- Local-only processing, no network calls
- Cross-platform via `tkinter`
- Pluggable actions with confidence-based selection
- Auto-apply the best action and write back to clipboard

## Quick Start
- Requirements: Python 3.9+
- Run: `python3 run.py`
- Try:
  - Copy CSV like `name,age\nAlice,30\nBob,25` → clipboard switches to JSON
  - Copy messy Markdown → clipboard is cleaned

## Typical Actions
- CSV → JSON (`copilot/plugins/csv_to_json.py`)
- Clean Markdown (`copilot/plugins/clean_markdown.py`)

## Architecture
- Watcher: `copilot/clipboard.py` monitors clipboard and writes results
- Orchestration: `copilot/main.py` loads plugins, ranks actions, applies top
- Rules: `copilot/rules.py` simple engine using `confidence(text)`
- Plugins: `copilot/plugins/` directory auto-discovered on import

Key references:
- `run()` entrypoint in `copilot/main.py:7`
- Change handling and apply in `copilot/main.py:11-22`
- Clipboard polling loop in `copilot/clipboard.py:22-33`
- CSV detection and conversion in `copilot/plugins/csv_to_json.py:7-26`
- Markdown cleaning in `copilot/plugins/clean_markdown.py:15-31`

## Plugins
Add a new plugin by creating a file under `copilot/plugins/` that defines a class with `name`, `confidence(text) -> float`, and `apply(text) -> str`.

Example skeleton:
```python
from ..rules import ActionPlugin

class MyPlugin(ActionPlugin):
    name = "my_plugin"
    def confidence(self, text: str) -> float:
        return 0.0
    def apply(self, text: str) -> str:
        return text
```
Plugins are auto-loaded at startup from the `copilot/plugins` package.

## Development
- Start: `python3 run.py`
- Adjust polling interval in `copilot/clipboard.py:7`
- Print applied actions in the terminal (`applied:<name>`) for quick feedback

## Roadmap
- UI overlay to pick actions instead of auto-apply
- Per-app profiles (editor vs browser behavior)
- More actions: remove tracking params, extract tables, normalize whitespace

## Privacy
All processing is local. No clipboard data leaves your machine.