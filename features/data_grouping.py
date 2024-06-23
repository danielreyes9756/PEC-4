# Ejercicio 3: Agrupamiento de datos.
import pandas as pd


# Ejercicio 3.1.
def group_by_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por 'state' y 'yeaar', calculando los totales acumulados.

    :param df: El DataFrame original.
    :return: El DataFrame agrupado por 'year' y 'state'.
    """
    print(df.head())
    grouped_df: pd.DataFrame = df.groupby(['year', 'state']).sum().reset_index()
    print("Primeras cinco filas del DataFrame tras agrupar las variables 'year' y 'state':")
    print(grouped_df.head())
    return grouped_df


# Ejercicio 3.2.
def print_biggest_handguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado ('state') y el año ('year') con el mayor número de 'handgun'.

    :param df: El DataFrame agrupado por 'year' y 'state'.
    :return: None.
    """
    __print_biggest_guns(df, 'handgun')


# Ejercicio 3.3.
def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado ('state') y el año ('year') con el mayor número de 'long_gun'.

    :param df: El DataFrame agrupado por 'year' y 'state'.
    :return: None.
    """
    __print_biggest_guns(df, 'longgun')


# Función auxiliar para los ejercicios 3.2 y 3.3.
def __print_biggest_guns(df: pd.DataFrame, gun_type: str) -> None:
    """
    Imprime el estado ('state') y el año ('year') con el mayor número de
    un tipo de arma especifica.

    :param df: El DataFrame agrupado por 'year' y 'state'.
    :param gun_type: El tipo de arma que se desea observar.
    :return: None.
    """
    guns: pd.Series = df.loc[df[gun_type].idxmax()]
    print(f"\nEl mayor número de armas tipo '{gun_type}' se registró en "
          f"{guns['year']}, contaban con un total de {guns[gun_type]} unidades.")
