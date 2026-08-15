# Restructuration TF-IDF — Squelette de projet (à compléter)

Vous avez, au **Module 1 (Brief 1)**, construit un classifieur d'intentions
Banking77 « tout-en-un » dans un notebook. Ici, vous **ne changez pas la
logique** : vous la **restructurez** dans l'architecture de projet du
**Module 4** (package `src/` modulaire piloté par un notebook guidé).

Aucune nouvelle conception, aucun nouveau modèle : vous redistribuez votre
code existant dans les bons modules, et vous nommez au passage les décisions
qu'il contenait déjà.

## Installation
```bash
pip install -r requirements.txt
```

## Données
Voir `data/README.md`. Placez le CSV Banking77 (`data/banking77.csv`, colonnes
`text,label`) ; en son absence, le chargement lève une erreur explicite.

## Comment travailler
Le notebook `notebooks/restructuration_intentions.ipynb` est le fil conducteur.
Il appelle les fonctions de `src/`, que vous complétez dans cet ordre :

| Ordre | Fichier | TODO | Ce que vous y remettez |
|---|---|---|---|
| 1 | `src/config.py`     | A-B | Indiquer la colonne texte et la colonne cible ; centraliser tous les réglages |
| 2 | `src/features.py`   | E-F | Votre découpage **stratifié** + votre **TF-IDF** (ajusté sur le train) |
| 3 | `src/models.py`     | G   | Votre modèle du Module 1 + ≥ 2 autres familles, en Pipelines |
| 4 | `src/evaluation.py` | H   | Vos métriques, choisies pour le **multi-classe déséquilibré** |
| 5 | `notebooks/…`       | —   | Exécuter, lire, conclure |

Une fois les `src/` complétés :
```bash
python -m src.benchmark      # écrit outputs/results.csv
```

## Fournis (ne pas modifier)
`src/data_loading.py`, `src/benchmark.py`.

## Arborescence
```
.
├── data/               banking77.csv (requis) + README
├── notebooks/
│   └── restructuration_intentions.ipynb
├── src/
│   ├── config.py       ← TODO A-B
│   ├── data_loading.py  (fourni)
│   ├── features.py     ← TODO E-F
│   ├── models.py       ← TODO G
│   ├── evaluation.py   ← TODO H
│   └── benchmark.py     (fourni → outputs/results.csv)
└── outputs/
```

