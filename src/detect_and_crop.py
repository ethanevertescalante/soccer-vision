"""Detect people with YOLO and crop them.

Reads:  data/raw/
Writes: data/crops/<player_id>/<image_id>_<n>.jpg
        data/metadata/crops.csv (crop_id, image_id, player_id, box, confidence)
Notes:  keep only the 'person' class; keep the largest/most central box or
        flag multi-person images for manual review.
Run:    python -m src.detect_and_crop
"""


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
