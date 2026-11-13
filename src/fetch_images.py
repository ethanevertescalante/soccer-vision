"""Download any image listed in images.csv whose file is missing.

Reads:  data/metadata/images.csv (path, source_url)
Writes: data/raw/<player_id>/<image_id>.jpg, resized to ~1024 px longest side
Logs:   reports/fetch_errors.csv for links that fail or are not images
Run:    python -m src.fetch_images
"""


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
