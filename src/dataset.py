"""Datasets, transforms and dataloaders (imported by train.py / evaluate.py)."""


def get_transforms(train: bool, image_size: int = 224):
    """Train: random resized crop, flip, color jitter. Eval: resize + normalize."""
    raise NotImplementedError


def get_dataloaders(cfg: dict):
    """Return {'train': DataLoader, 'val': ..., 'test': ...} and class_to_idx."""
    raise NotImplementedError
