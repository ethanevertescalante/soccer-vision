"""Split crops into train/val/test, grouped by event.

Reads:  data/metadata/crops.csv joined with images.csv (for 'event')
Writes: data/splits/{train,val,test}/<player_id>/
Notes:  use sklearn GroupShuffleSplit with groups=event and config.SEED so a
        whole match lands in exactly one split. Print counts per player/split.
Run:    python -m src.make_splits
"""


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
