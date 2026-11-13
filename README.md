# Soccer Vision

Recognize 10 Premier League players in photos: YOLO finds people, a ResNet
classifier identifies them, and player info comes from `players.csv` / PostgreSQL.

CSC 671/871 Deep Learning, Fall 2026 · Ethan Escalante, Boshra Alzindeni, Saeed Qazi

## Layout
```
data/metadata/   players.csv, images.csv, crops.csv (committed)
data/raw/        original images, one folder per player_id
data/crops/      YOLO person crops (generated)
data/splits/     train/val/test folders the CNN trains on (generated)
configs/         one yaml per experiment
src/             pipeline scripts (see below)
models/          trained weights per run (not committed)
reports/         metrics, plots, runs.csv
notebooks/       exploration only
```

## Pipeline
```
pip install -r requirements.txt
python -m src.check_data        # every CSV row has a file and vice versa
python -m src.fetch_images      # download missing images from source_url
python -m src.detect_and_crop   # raw -> crops
python -m src.make_splits       # crops -> splits (grouped by event)
python -m src.train --config configs/train.yaml
python -m src.evaluate --run models/resnet18_baseline --split test
python -m src.predict some_photo.jpg --run models/resnet18_baseline
```

## images.csv columns
`image_id, player_id, path, source_url, event, date, kit, view`
- `event`: `YYYY-MM-DD_HOME-AWAY` (or `photoshoot`, `training`)
- `kit`: `home_club | away_club | old_club | national | training`
