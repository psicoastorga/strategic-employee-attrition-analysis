# Archivo: src/data/cleaning.py
# Limpieza inicial del dataset de rotación de empleados

import pandas as pd

# Eliminación de columnas con valor constante
def drop_constant_columns(df):
    return df.drop(columns=['EmployeeCount','Over18','StandardHours'])

# Eliminación de identificadores
def drop_id_columns(df):
    return df.drop(columns=['EmployeeNumber'])
