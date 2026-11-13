"""Evaluate a trained run on the test (or val) split.

Reads:  models/<run_name>/, data/splits/test
Writes: reports/<run_name>/ (classification report, confusion matrix, loss
        curves, misclassified crops) and appends one line to reports/runs.csv
Run:    python -m src.evaluate --run models/<run_name> --split test
"""


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
