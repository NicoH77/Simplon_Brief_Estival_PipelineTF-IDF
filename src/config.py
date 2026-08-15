"""
config.py — Configuration centralisée du projet.

Regroupez ici TOUS les réglages : plus aucune valeur ni chemin ne doit être
codé en dur ailleurs dans le code. C'est le point d'entrée unique de la
configuration (un des marqueurs d'un code propre : on sait où regarder).
"""

RANDOM_SEED = 42

# --- Schéma des données (colonnes de data/banking77.csv) --------------------
# TODO A : la colonne contenant le message client (l'entrée du modèle)
TEXT_COL = ...   # TODO A

# TODO B : la colonne contenant l'intention à prédire (la cible)
LABEL_COL = ...  # TODO B

# --- Découpage --------------------------------------------------------------
TEST_SIZE = 0.25

# --- Sorties ----------------------------------------------------------------
RESULTS_PATH = "outputs/results.csv"
