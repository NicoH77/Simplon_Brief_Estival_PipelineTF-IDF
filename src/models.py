"""
models.py — Liste raisonnée de candidats (parallèle du models.py du Module 4).

Au Module 1 vous aviez UN modèle. Le Module 4 en demande au moins TROIS
familles, comparées. Encapsulez chacun avec le TF-IDF dans un Pipeline : cela
garantit l'ajustement du vectoriseur sur le train uniquement.
"""

from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

from .features import make_vectorizer


def build_candidates() -> dict[str, Pipeline]:
    """
    Construit les pipelines candidats à comparer.

    Retour
    ------
    dict[str, Pipeline]
        Dictionnaire de la forme :
        {
            "logreg": Pipeline(...),
            "linear_svm": Pipeline(...),
            "multinomial_nb": Pipeline(...)
        }
    """

    """TODO G : renvoyer {nom: Pipeline(tfidf -> modèle)} pour >= 3 familles.

    Incluez le modèle de votre Module 1, puis au moins deux autres familles
    adaptées à du texte creux (par ex. SVM linéaire, Naive Bayes multinomial).
    Chaque Pipeline : Pipeline([("tfidf", make_vectorizer()), ("clf", <modèle>)]).
    """
    # TODO G
    return {
        "logreg": Pipeline(
            [
                ("tfidf", make_vectorizer()),
                ("clf", LogisticRegression(max_iter=1000)),
            ]
        ),
        "linear_svm": Pipeline(
            [
                ("tfidf", make_vectorizer()),
                ("clf", LinearSVC()),
            ]
        ),
        "naive_bayes": Pipeline(
            [
                ("tfidf", make_vectorizer()),
                ("clf", MultinomialNB()),
            ]
        ),
    }
