"""Load configs/config.yaml and resolve paths relative to the project root."""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_config(path: str | Path = ROOT / "configs" / "config.yaml") -> dict:
    cfg = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    cfg["paths"] = {k: ROOT / v for k, v in cfg["paths"].items()}
    return cfg
