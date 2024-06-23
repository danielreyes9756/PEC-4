# PEC-4

Este proyecto realiza un análisis de datos sobre las ventas de armas de fuego en Estados Unidos utilizando datos del sistema de verificación de antecedentes de compradores (NICS, National Instant Criminal Background Check System). A continuación se detallan los diferentes aspectos y funcionalidades del proyecto

## Pasos Para Poder Ejecutar El Proyecto
En este caso copiar o clonar el proyecto no es necesario no obstante debera agregar a la carpeta "PEC-4/datasets" los ficheros de datos necesarios para esta practica, a su vez también sera necesario crear y iniciar un environtment antes de instalar los requisitos.
1. cd ./PEC-4
2. pip install -r requirements.txt
3. copie los ficheros necesario en "PEC-4/datasets":
    * nics-firearm-background-checks.csv
    * us-state-populations.csv
    * us-states.json
4. Ejecutar el siguiente comando en la termina
```bash
python3 main.py
```

## Contenido del Proyecto (Feautures)

### Funciones de Lectura y Limpieza de Datos:
* **read_csv**: Función para leer un fichero CSV y mostrar las cinco primeras filas y la estructura del DataFrame.
* **clean_csv**: Limpia el DataFrame eliminando todas las columnas a excepción de mes, estado, permiso, armas cortas y largas.
* **rename_col**: Función para renombrar la columna de armas de largas en el DataFrame (inicialmente cuenta con un nombre incorrecto).

### Funciones de Procesamiento de Datos:
* **breakdown_date**: Función para desglosar la columna de fechas en año y mes.
* **erase_month**: Función para eliminar la columna de mes del DataFrame.

### Funciones de Agrupamiento:
* **groupby_state_and_year**: Función para agrupar los datos por estado y año.
* **print_biggest_handguns**: Función para imprimir el estado y año con más ventas de pistolas.
* **print_biggest_longguns**: Función para imprimir el estado y año con más ventas de rifles largos.

### Análisis Temporal:

* **time_evolution**: Función para generar un gráfico de la evolución temporal de las licencias y ventas de armas, además muestra un breve análisis por consola, la imagen del gráfico en cuestiión se almacenara en la carpeta "PEC-4/plots".

### Análisis de los Estados:
* **groupby_state**: Función para agrupar los datos solo por estado y mostrar valores totales.
* **clean_states**: Función para eliminar estados no incluidos en un archivo de población.
* **merge_datasets**: Función para fusionar datos de ventas y datos de población por estado.
* **calculate_relative_values**: Función para calcular valores relativos basados en la población.

### Mapas Coropléticos:

* **create_choropleth_map**: Función que genera mapas coropléticos utilizando Folium para visualizar permit_perc, handgun_perc y longgun_perc.
* **save_map_as_image**: Función que guarda los mapas como imagenes (No funciona).

## Contenido del Proyecto (Testing)
El proyecto a su vez cuenta con pruebas unitarias para cubrir cada una de las funciones anteriormente propuestas.

Se ha empleado la libreria HTMLTestRunner para generar reportes.

Tan solo ejecutando el siguiente código en nuestra terminal se procedera a crear una carpeta reports conteniendo los ficheros HTML, css y JavaScript necesarios para visualizar estos.

```bash
python3 test_runner.py
```

La carpeta reports se encuentra bajo la carpeta PEC-4.

## Estructura del Proyecto
He decidido emplear una estructura de capas, pero liviana sin anidar y engorronar tanto la estructura esto debido a que contamos con un proyecto bastante pequeño, y esta estructura es lo suficientemente limpia y clara como para mantener un entendimiento claro del proyecto a la vez que una buena estetica.
```
PEC-4/
├── datasets/
│   ├── nics-firearm-background-checks.csv
│   ├── us-state-populations.csv
│   ├── us-states.json
├── features/
│   ├── __init__.py
│   ├── data_cleanup.py
│   ├── data_grouping.py
│   ├── data_maps_creator.py
│   ├── data_processing.py
│   ├── data_status_analysis.py
│   ├── data_temporal_analysis.py
├── plots/  (solo tras ejecutar)
│   ├── time_evolution.png
├── reports/  (solo tras ejecutar test)
├── tests/
│   ├── plots/  (solo tras ejecutar test)
│   │   ├── time_evolution.png
│   ├── __init__.py
│   ├── test_data_cleanup.py
│   ├── test_data_grouping.py
│   ├── test_data_maps_creator.py
│   ├── test_data_processing.py
│   ├── test_data_status_analysis.py
│   ├── test_data_temportal_analysis.py
├── README.md
├── requirements.txt
└── main.py
└── test_runnner.py
```