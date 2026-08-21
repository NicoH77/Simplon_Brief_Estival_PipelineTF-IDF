"""
benchmark.py — Orchestration (FOURNI). Reproduit le geste du Module 4 :
charge -> découpe -> entraîne chaque candidat -> évalue -> écrit outputs/results.csv

Lancement :  python -m src.benchmark
"""

from __future__ import annotations

import os

import pandas as pd

from . import config, data_loading, evaluation, features, models


def run() -> pd.DataFrame:
    df = data_loading.load()

    X_train, X_test, y_train, y_test = features.make_split(df)
    candidates = models.build_candidates()

    rows = []
    for name, pipe in candidates.items():
        pipe.fit(X_train, y_train)  # TF-IDF ajusté sur le TRAIN seul
        y_pred = pipe.predict(X_test)
        metrics = evaluation.evaluate(y_test, y_pred)
        metrics["model"] = name
        rows.append(metrics)
        print(
            f"[benchmark] {name:16s} "
            f"macro_f1={metrics['f1_macro']:.3f}  acc={metrics['accuracy']:.3f}"
        )

    results = pd.DataFrame(rows).set_index("model").sort_values("f1_macro", ascending=False)

    os.makedirs("outputs", exist_ok=True)
    results.to_csv(config.RESULTS_PATH)
    print(f"[benchmark] résultats écrits dans {config.RESULTS_PATH}")
    return results


if __name__ == "__main__":
    run()
