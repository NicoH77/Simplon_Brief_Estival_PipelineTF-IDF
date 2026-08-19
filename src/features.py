"""
features.py — Découpage stratifié + préprocesseur (parallèle du features.py M4).

Reprenez ici ce que vous aviez fait au Module 1 : le découpage train/test et
la vectorisation TF-IDF. Deux gestes de conception à ne pas manquer :
  - le découpage doit être STRATIFIÉ sur l'intention (sinon les classes rares
    peuvent disparaître du test) ;
  - le TF-IDF doit être ajusté sur le TRAIN uniquement (geste anti-fuite du
    Module 4). Le Pipeline de models.py s'en charge si vous renvoyez ici un
    vectoriseur NON ajusté.
"""
from __future__ import annotations
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from . import config


def make_split(df: pd.DataFrame):
    """TODO E : découpage STRATIFIÉ train/test sur l'intention.

    Renvoyez X_train, X_test, y_train, y_test en n'utilisant que la colonne
    texte (config.TEXT_COL) comme X et config.LABEL_COL comme y.
    """
    # TODO E
    # raise NotImplementedError

    X = df[config.TEXT_COL].astype(str)
    y = df[config.LABEL_COL]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.TEST_SIZE,
        random_state=config.RANDOM_SEED,
        shuffle=True,
        stratify=y,
    )
 
    return X_train, X_test, y_train, y_test
    


def make_vectorizer() -> TfidfVectorizer:
    """TODO F : renvoyer le TfidfVectorizer de votre Module 1 (NON ajusté).

    Reprenez vos réglages (ngrams, min_df, lowercase, ...). Ne pas appeler
    .fit() ici : le Pipeline l'ajustera sur le train.
    """
    # TODO F
    return TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95,
    )
