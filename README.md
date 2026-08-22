# Restructuration TF-IDF

## Objectif
L'objectif de ce projet est de construire un classifieur d'intentions à partir du jeu de données **Banking77**.
Le notebook initial a été restructuré afin de séparer les responsabilités dans plusieurs modules Python :
- chargement des données ;
- extraction des caractéristiques ;
- définition des modèles ;
- évaluation ;
- benchmark.
Le notebook ne sert plus qu'à l'orchestration et à l'expérimentation.

## Installation
```bash
pip install -r requirements.txt
```

## Données
Voir `data/README.md`. Placez le CSV Banking77 (`data/banking77.csv`, colonnes
`text,label`) ; en son absence, le chargement lève une erreur explicite.

## Architecture
Le notebook `notebooks/restructuration_intentions.ipynb` est le fil conducteur.
Il appelle les fonctions de `src/`, complétées dans cet ordre :

| Ordre | Fichier | TODO | Ce que vous y remettez |
|---|---|---|---|
| 1 | `src/config.py`     | A-B | Indique la colonne texte et la colonne cible ; centralise tous les réglages |
| 2 | `src/features.py`   | E-F | Découpage **stratifié** + **TF-IDF** (ajusté sur le train) |
| 3 | `src/models.py`     | G   | Modèle du Module 1 + ≥ 2 autres familles, en Pipelines |
| 4 | `src/evaluation.py` | H   | Métriques, choisies pour le **multi-classe déséquilibré** |
| 5 | `notebooks/…`       | —   | ordonnancement, observations, conclusions |



## Fournis (ne pas modifier)
`src/data_loading.py`, `src/benchmark.py`.

## Arborescence
```
.
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── banking77.csv
├── notebooks/
│   └── restructuration_intentions.ipynb
├── outputs/
│   └── results.csv
├── src/
│   ├── benchmark.py
│   ├── config.py
│   ├── data_loading.py
│   ├── evaluation.py
│   ├── features.py
│   └── models.py
├── tests/
│   └── test_smoke.py
├── Makefile
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Benchmark

Les trois familles de modèles suivantes sont comparées :
- Logistic Regression => Régression linéaire
- Linear SVM => Machines à vecteurs de support
- Multinomial Naive Bayes => Modèle probabiliste

Une fois les `src/` complétés :

```bash
python -m src.benchmark      # écrit outputs/results.csv
```

## Contrôle qualité
Le projet utilise :
- Ruff pour le formatage ;
- Ruff pour l'analyse statique ;
- Pytest pour les tests automatisés.

## Test de fumée
Un test de fumée vérifie que le pipeline principal fonctionne toujours.
Le test contrôle :
- l'import du module src.benchmark ;
- l'exécution de la fonction run() ;
- la génération de outputs/results.csv.



