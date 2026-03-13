# src/data/preprocessing.py

import pandas as pd

BINARY_MAP = {
    'Attrition': {'No':0,'Yes':1},
    'Gender': {'Male':0,'Female':1},
    'OverTime': {'No':0,'Yes':1}
}


def encode_binary_variables(df: pd.DataFrame) -> pd.DataFrame:
    """Encode binary categorical variables."""

    for col, mapping in BINARY_MAP.items():
        df[col] = df[col].map(mapping)

    return df


ORDINAL_COLUMNS = [
    'Education',
    'JobInvolvement',
    'PerformanceRating'
]


def convert_ordinal_variables(df: pd.DataFrame) -> pd.DataFrame:
    """Convert ordinal variables to ordered categories."""

    for col in ORDINAL_COLUMNS:
        df[col] = pd.Categorical(df[col], ordered=True)

    return df


CATEGORICAL_COLUMNS = [
    'BusinessTravel',
    'Department',
    'EducationField',
    'JobRole',
    'MaritalStatus'
]


def convert_categorical_variables(df: pd.DataFrame) -> pd.DataFrame:
    """Convert nominal variables to categorical dtype."""

    df[CATEGORICAL_COLUMNS] = df[CATEGORICAL_COLUMNS].astype('category')

    return df
