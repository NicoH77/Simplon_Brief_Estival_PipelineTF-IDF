#!/usr/bin/env python3

from datasets import load_dataset, concatenate_datasets, Features, Value

DATASET_ID = "PolyAI/banking77"
OUTPUT_CSV = "banking77.csv"


def main() -> None:
    # 1) Charge toutes les partitions disponibles du dataset Hugging Face.
    #    Aujourd'hui, la carte officielle liste train et test.
    dataset_dict = load_dataset(
        "parquet",
        data_files={
            "train": "https://huggingface.co/datasets/PolyAI/banking77/resolve/main/train-00000-of-00001.parquet",
            "test": "https://huggingface.co/datasets/PolyAI/banking77/resolve/main/test-00000-of-00001.parquet",
        },
    )

    required_columns = {"text", "label"}
    splits = list(dataset_dict.keys())

    # 2) Sélectionne uniquement les colonnes demandées, dans l'ordre demandé.
    parts = []
    for split_name in splits:
        split_ds = dataset_dict[split_name]

        missing = required_columns - set(split_ds.column_names)
        if missing:
            raise ValueError(
                f"Partition {split_name!r}: colonnes manquantes {sorted(missing)}. "
                f"Colonnes disponibles: {split_ds.column_names}"
            )

        parts.append(split_ds.select_columns(["text", "label"]))

    # 3) Fusionne toutes les partitions disponibles.
    full_ds = concatenate_datasets(parts)

    # 4) Force un schéma simple text:string, label:int64.
    #    Important : int(x) conserve l'identifiant numérique du label.
    #    On n'utilise jamais int2str(), donc les labels textuels ne sont pas exportés.
    full_ds = full_ds.map(
        lambda batch: {
            "text": batch["text"],
            "label": [int(x) for x in batch["label"]],
        },
        batched=True,
        features=Features(
            {
                "text": Value("string"),
                "label": Value("int64"),
            }
        ),
        desc="Normalisation du schéma text,label",
    )

    # 5) Sécurité : ordre exact des colonnes du CSV final.
    full_ds = full_ds.select_columns(["text", "label"])

    # 6) Écrit le CSV final.
    full_ds.to_csv(OUTPUT_CSV)

    # 7) Contrôles simples.
    assert full_ds.column_names == ["text", "label"]
    sample = full_ds[: min(20, len(full_ds))]
    assert all(isinstance(x, int) for x in sample["label"])

    print(f"Fichier écrit : {OUTPUT_CSV}")
    print(f"Partitions fusionnées : {splits}")
    print(f"Nombre de lignes : {len(full_ds)}")
    print(f"Colonnes : {full_ds.column_names}")
    print(f"Features : {full_ds.features}")


if __name__ == "__main__":
    main()