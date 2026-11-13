"""Shared paths and constants. Import from here instead of hard-coding paths."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
METADATA = DATA / "metadata"
RAW = DATA / "raw"
CROPS = DATA / "crops"
SPLITS = DATA / "splits"
MODELS = ROOT / "models"
REPORTS = ROOT / "reports"
CONFIGS = ROOT / "configs"

PLAYERS_CSV = METADATA / "players.csv"
IMAGES_CSV = METADATA / "images.csv"
CROPS_CSV = METADATA / "crops.csv"

SEED = 42
SPLIT_FRACTIONS = {"train": 0.70, "val": 0.15, "test": 0.15}
UNKNOWN_THRESHOLD = 0.6  # predict.py: below this top probability -> "unknown"
