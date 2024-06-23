# Ejercicio 2: Procesamiento de datos.
import pandas as pd


# Ejercicio 2.1.
def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame eliminando todas las columnas a excepción
    de 'month', 'state', 'permit', 'handgun', 'long_gun'.

    :param df: El DataFrame original.
    :return: El DataFrame tras limpiar las columnas no necesarios.
    """
    df[['year', 'month']] = df['month'].str.split('-', expand=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    print("Primeras cinco filas del DataFrame después de dividir 'month' en 'year' y 'month':")
    print(df.head())
    return df


# Ejercicio 2.2
def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna 'month' del DataFrame.

    :param df: El DataFrame con la columna 'month'.
    :return: El DataFrame con la columna 'month' eliminada.
    """
    df.drop(columns='month', inplace=True)
    print("\nPrimeras cinco filas del DataFrame tras eliminar la columna 'month':")
    print(df.head())
    print("\nColumnas del DataFrame tras eliminar la columna 'month':")
    print(df.columns)
    return df
