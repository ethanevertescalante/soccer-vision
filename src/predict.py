"""Full pipeline on one image: YOLO -> crop -> classifier -> player lookup.

Returns a list of {box, player_id, confidence}; player_id is "unknown" when the
top probability is below config.UNKNOWN_THRESHOLD.
Run:    python -m src.predict path/to/image.jpg --run models/<run_name>
"""


def predict(image_path, run_dir):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
