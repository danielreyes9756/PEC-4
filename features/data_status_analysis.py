# Ejercicio 5: Análisis de los estados.
import pandas as pd
from typing import List


# Ejercicio 5.1.
def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por estado y muestra los valores totales.

    :param df: DataFrame con los datos agrupados por 'state' y 'year'.
    :return: DataFrame con los valores agrupados únicamente por estados.
    """
    df_grouped: pd.DataFrame = df.groupby('state').sum().reset_index()

    # He decidido agregar esta línea ya que el campo 'year' deja
    # de tener sentido, debido a que se suman los campos.
    df_grouped.drop(columns='year', inplace=True)
    print("Primeras 5 filas del DataFrame agrupado por estado:")
    print(df_grouped.head())
    return df_grouped


# Ejercicio 5.2.
def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina los estados 'Guam', 'Mariana Islands', 'Puerto Rico' y 'Virginia Islands' del DataFrame.

    :param df: DataFrame con los datos agrupados por 'states'.
    :return: DataFrame sin los estados mencionados.
    """
    states_to_remove: List[str] = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virginia Islands']
    df_cleaned: pd.DataFrame = df[~df['state'].isin(states_to_remove)]
    df_cleaned.reset_index(drop=True, inplace=True)
    print(f"\nNúmero de estados tras la limpieza: {len(df_cleaned)}.")
    return df_cleaned


# Ejercicio 5.3.
def merge_datasets(df_firearms: pd.DataFrame, df_population: pd.DataFrame) -> pd.DataFrame:
    """
    Fusiona los datos del DataFrame de armas de fuego y los datos del DataFrame poblacionales por estados.
    
    :param df_firearms: DataFrame con los datos de las armas de fuego.
    :param df_population: DataFrame con los datos poblacionales.
    :return: DataFrame resultante de la fusión.
    """
    df_merged: pd.DataFrame = pd.merge(df_firearms, df_population, on='state')
    print("\nPrimeras 5 filas del Dataframe tras la fusión:")
    print(df_merged.head())
    return df_merged


# Ejercicio 5.4.
def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los valores relativos de los porcentajes de permisos, armas cortas y armas largas.

    :param df: DataFrame con los datos de las armas de fuego y la población.
    :return: DataFrame con las columnas de valores porcentuales solicitadas.
    """
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['longgun'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    print("\nPrimeras 5 filas del Dataframe tras haber agregado las nuevas columnas relativasla fusión:")
    print(df.head())
    return df


# Ejercicio 5.5.
def analyze_kentucky(df: pd.DataFrame) -> None:
    """
    Realiza el análisis de los valores relativos de Kentucky.

    :param df: DataFrame con los datos relativos de armas de fuego y la población en Kentucky.
    :return: None.
    """
    mean_permit_perc: pd.Series = df['permit_perc'].mean()
    print(f"\nMedia de permisos: {mean_permit_perc:.2f}")

    print("\nInformación relativa al estado Kentucky:")
    print(df[df['state'] == 'Kentucky'])

    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_perc

    new_mean_permit_perc: pd.Series = df['permit_perc'].mean()
    print(f"\nMedia de permisos despues de reemplazar Kentucky: {new_mean_permit_perc:.2f}")

    print("\nConclusiones:")
    print("El valor de porcentaje de permisos ha cambiado después de reemplazar el valor de Kentucky.")
    print("Esto muestra cómo los outliers pueden afectar las métricas estadísticas.")
