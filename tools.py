#tools.py

import pandas as pd
import json

# État global du dataframe
DATAFRAME = None


def load_csv(path):
    global DATAFRAME
    DATAFRAME = pd.read_csv(path)
    return f"Loaded dataframe with {DATAFRAME.shape[0]} rows and {DATAFRAME.shape[1]} columns."


def describe_dataframe():
    global DATAFRAME

    desc = {
        "shape": DATAFRAME.shape,
        "columns": {}
    }

    for col in DATAFRAME.columns:
        series = DATAFRAME[col]
        desc["columns"][col] = {
            "dtype": str(series.dtype),
            "nulls": int(series.isna().sum()),
            "null_percent": float(series.isna().mean()),
            "unique": int(series.nunique()),
        }

        if pd.api.types.is_numeric_dtype(series):
            desc["columns"][col].update({
                "mean": float(series.mean()),
                "std": float(series.std()),
                "min": float(series.min()),
                "max": float(series.max())
            })

    return json.dumps(desc, indent=2)


def clean_column(column, strategy):
    global DATAFRAME

    if strategy == "drop":
        DATAFRAME = DATAFRAME.drop(columns=[column])
        return f"Column {column} dropped."

    if strategy == "median":
        median = DATAFRAME[column].median()
        DATAFRAME[column] = DATAFRAME[column].fillna(median)
        return f"Filled NaN in {column} with median = {median}"

    if strategy == "mean":
        mean = DATAFRAME[column].mean()
        DATAFRAME[column] = DATAFRAME[column].fillna(mean)
        return f"Filled NaN in {column} with mean = {mean}"

    if strategy == "mode":
        mode = DATAFRAME[column].mode()[0]
        DATAFRAME[column] = DATAFRAME[column].fillna(mode)
        return f"Filled NaN in {column} with mode = {mode}"

    return "Unknown strategy"


def save_report(path):
    global DATAFRAME
    DATAFRAME.to_csv(path, index=False)
    return f"Saved cleaned dataset to {path}"

