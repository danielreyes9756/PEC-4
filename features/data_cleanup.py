# Ejercicio 1: Lectura y limpieza de datos.
import pandas as pd
from typing import List


# Ejercicio 1.1.
def read_csv(url: str) -> pd.DataFrame:
    """
    Lee un fichero CSV y muestra las cinco primeras filas y la estructura del DataFrame.

    :param url: La URL del fichero CSV a leer.
    :return: El DataFrame basado en el fichero leido.
    """
    df: pd.DataFrame = pd.read_csv(url)
    print("Primeras cinco filas del DataFrame:")
    print(df.head())
    print("\nEstructura del DataFrame:")
    df.info()
    return df


# Ejercicio 1.2.
def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame eliminando todas las columnas a excepción de 'month',
    'state', 'permit', 'handgun' y 'long_gun'.

    :param df: El DataFrame original.
    :return: El DataFrame tras limpiar las columnas anteriormente nombradas.
    """
    columns: List[str] = ['month', 'state', 'permit', 'handgun', 'long_gun']
    df_cleaned: pd.DataFrame = df[columns].copy()
    print(f"\nEstructura del DataFrame tras la limpieza de los los campos {columns}:")
    print(df_cleaned.columns)
    return df_cleaned


# Ejercicio 1.3
def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra la columna  'long_gun' a 'longgun' en el DataFrame.

    :param df: El DataFrame con las columnas limpias.
    :return: El DataFrame con la columna 'long_gun' renombrada a 'longgun'.
    """
    if 'long_gun' in df.columns:
        df.rename(columns={'long_gun': 'longgun'}, inplace=True)

    print("\nColumnas del DataFrame tras renombrar la columna 'long_gun' a 'longgun':")
    print(df.columns)
    return df
