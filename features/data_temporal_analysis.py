# Ejercicio 4: Análisis temporal.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict


# Ejercicio 4.1.
def time_evolution(df: pd.DataFrame) -> None:
    """
    Crea un gráfico que muestra la evolución temporal del número total de permisos, armas cortas y armas largas.

    :param df: DataFrame con las columnas año, permiso, armas cortas y armas largas.
    :return: None.
    """
    df_gropued = df.groupby('year').sum().reset_index()
    save_path: str = 'plots/time_evolution.png'
    columns_and_labels: Dict[str, str] = {'permit': 'Permits', 'handgun': 'Hand Guns', 'longgun': 'Long Guns'}

    plt.figure(figsize=(14, 7))

    for column, label in columns_and_labels.items():
        sns.lineplot(data=df_gropued, x='year', y=column, label=label)

    plt.title("Time Evolution of Permits, Hand Guns and Long Guns")
    plt.xlabel("Year")
    plt.ylabel("Total Count")
    plt.legend()
    plt.grid(True)

    plt.savefig(save_path)
    print(f"El entorno no es interactivo por lo que se ha guardado la imagen en: '{save_path}'")
    print("\n Breve analisis, tras observar la gráfica podemos apreciar lo siguiente:")
    print("\n La tenencia de armas largas es menor, respecto que la cantidad de "
          "permisos otorgados y la cantidad de armas cortas, por otro lado todos "
          "los campos tuvieron un auge o aumento por el 2016 y ha ido reduciendose "
          "llegando casí a sus mínimos historicos en 2020.")
