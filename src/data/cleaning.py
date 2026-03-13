# src/data/cleaning.py

import pandas as pd

CONSTANT_COLUMNS = ['EmployeeCount', 'Over18', 'StandardHours']
ID_COLUMNS = ['EmployeeNumber']


def drop_constant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove columns with constant values."""
    return df.drop(columns=CONSTANT_COLUMNS)


def drop_id_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove identifier columns."""
    return df.drop(columns=ID_COLUMNS)
