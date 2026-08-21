"""
evaluation.py — Métriques qui résistent au déséquilibre (parallèle M4).

Attention : la fraude du Module 4 est BINAIRE (PR-AUC). Vous êtes ici en
MULTI-CLASSE faiblement déséquilibré. L'exactitude globale flatte le modèle
sur les classes fréquentes. Choisissez des métriques qui pèsent chaque
intention équitablement, et regardez le rappel PAR classe.
"""

from __future__ import annotations

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    recall_score,
)


def evaluate(y_true, y_pred) -> dict:
    """TODO H : renvoyer un dict de métriques robustes au déséquilibre.

    Incluez au minimum : accuracy, une métrique équilibrée entre classes
    (par ex. balanced_accuracy) et le macro-F1. Ajoutez le weighted-F1 pour
    comparer.
    """

    """
    Évalue un classifieur multi-classe à l'aide de métriques
    robustes au déséquilibre.

    Parameters
    ----------
    y_true : array-like
        Labels réels.
    y_pred : array-like
        Labels prédits.

    Returns
    -------
    dict
        Dictionnaire contenant les principales métriques.
    """

    labels = sorted(set(y_true))

    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "balanced_accuracy": balanced_accuracy_score(
            y_true,
            y_pred,
        ),
        "f1_macro": f1_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
        "f1_weighted": f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        ),
        "recall_macro": recall_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
        "recall_per_class": {
            label: round(float(score), 3)
            for label, score in zip(
                labels,
                recall_score(
                    y_true,
                    y_pred,
                    average=None,
                    labels=labels,
                    zero_division=0,
                ),
            )
        },
    }


def per_class_report(y_true, y_pred) -> pd.DataFrame:
    """Rapport par intention (fourni). Renvoie un DataFrame precision/recall/f1/support."""
    from sklearn.metrics import classification_report

    rep = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    return pd.DataFrame(rep).T
