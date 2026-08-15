"""
models.py — Liste raisonnée de candidats (parallèle du models.py du Module 4).

Au Module 1 vous aviez UN modèle. Le Module 4 en demande au moins TROIS
familles, comparées. Encapsulez chacun avec le TF-IDF dans un Pipeline : cela
garantit l'ajustement du vectoriseur sur le train uniquement.
"""
from __future__ import annotations
from sklearn.pipeline import Pipeline

from .features import make_vectorizer
from . import config


def build_candidates() -> dict[str, Pipeline]:
    """TODO G : renvoyer {nom: Pipeline(tfidf -> modèle)} pour >= 3 familles.

    Incluez le modèle de votre Module 1, puis au moins deux autres familles
    adaptées à du texte creux (par ex. SVM linéaire, Naive Bayes multinomial).
    Chaque Pipeline : Pipeline([("tfidf", make_vectorizer()), ("clf", <modèle>)]).
    """
    # TODO G
    raise NotImplementedError
