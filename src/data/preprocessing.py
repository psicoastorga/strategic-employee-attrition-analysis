# Archivo: src/data/preprocessing.py
# Transformaciones y codificación de variables

import pandas as pd

# Codificación de variables binarias
def encode_binary_variables(df):

    df['Attrition'] = df['Attrition'].map({'No':0,'Yes':1})
    df['Gender'] = df['Gender'].map({'Male':0,'Female':1})
    df['OverTime'] = df['OverTime'].map({'No':0,'Yes':1})

    return df


# Conversión de variables ordinales
def convert_ordinal_variables(df):

    df['Education'] = pd.Categorical(df['Education'], ordered=True)
    df['JobInvolvement'] = pd.Categorical(df['JobInvolvement'], ordered=True)
    df['PerformanceRating'] = pd.Categorical(df['PerformanceRating'], ordered=True)

    return df


# Conversión de variables categóricas
def convert_categorical_variables(df):

    cols = [
        'BusinessTravel',
        'Department',
        'EducationField',
        'JobRole',
        'MaritalStatus'
    ]

    df[cols] = df[cols].astype('category')

    return df
