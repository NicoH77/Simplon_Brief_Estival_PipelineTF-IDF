"""
data_loading.py — Chargement des données (FOURNI).

Charge le CSV Banking77 local (data/banking77.csv, schéma [text, label]).
Échoue explicitement si le fichier est absent.
"""

from __future__ import annotations

import os

import pandas as pd

_REAL_PATH = "data/banking77.csv"


def load() -> pd.DataFrame:
    """Retourne le DataFrame Banking77 (au moins les colonnes text et label)."""
    if not os.path.exists(_REAL_PATH):
        raise FileNotFoundError(
            f"Jeu de données introuvable : {_REAL_PATH}.\n"
            "Placez le CSV Banking77 (colonnes text,label) dans data/ "
            "— voir data/README.md."
        )
    df = pd.read_csv(_REAL_PATH)
    print(f"[data_loading] Banking77 chargé : {len(df)} lignes")
    return df
