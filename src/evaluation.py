"""
evaluation.py — Métriques qui résistent au déséquilibre (parallèle M4).

Attention : la fraude du Module 4 est BINAIRE (PR-AUC). Vous êtes ici en
MULTI-CLASSE faiblement déséquilibré. L'exactitude globale flatte le modèle
sur les classes fréquentes. Choisissez des métriques qui pèsent chaque
intention équitablement, et regardez le rappel PAR classe.
"""
from __future__ import annotations
import pandas as pd


def evaluate(y_true, y_pred) -> dict:
    """TODO H : renvoyer un dict de métriques robustes au déséquilibre.

    Incluez au minimum : accuracy, une métrique équilibrée entre classes
    (par ex. balanced_accuracy) et le macro-F1. Ajoutez le weighted-F1 pour
    comparer.
    """
    # TODO H
    raise NotImplementedError


def per_class_report(y_true, y_pred) -> pd.DataFrame:
    """Rapport par intention (fourni). Renvoie un DataFrame precision/recall/f1/support."""
    from sklearn.metrics import classification_report
    rep = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    return pd.DataFrame(rep).T
