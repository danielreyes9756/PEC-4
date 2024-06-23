import json

from features.data_cleanup import read_csv, clean_csv, rename_col
from features.data_processing import breakdown_date, erase_month
from features.data_grouping import group_by_state_and_year, print_biggest_handguns, print_biggest_longguns
from features.data_temporal_analysis import time_evolution
from features.data_status_analysis import groupby_state,\
    clean_states,\
    merge_datasets,\
    calculate_relative_values,\
    analyze_kentucky
from features.data_maps_creator import create_choropleth_map, save_map_as_image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url_nics_firearm = 'datasets/nics-firearm-background-checks.csv'

    print("---------- Ejercicio 1 ----------")
    df = read_csv(url_nics_firearm)
    df_cleaned = clean_csv(df)
    df_renamed = rename_col(df_cleaned)

    print("\n---------- Ejercicio 2 ----------")
    df_with_date = breakdown_date(df_renamed)
    df_without_month = erase_month(df_with_date)

    print("\n---------- Ejercicio 3 ----------")
    df_grouped_by_state_and_year = group_by_state_and_year(df_without_month)
    print_biggest_handguns(df_grouped_by_state_and_year)
    print_biggest_longguns(df_grouped_by_state_and_year)

    print("\n---------- Ejercicio 4 ----------")
    time_evolution(df_grouped_by_state_and_year)

    print("\n---------- Ejercicio 5 ----------")
    df_group_by_states = groupby_state(df_grouped_by_state_and_year)
    df_states_cleaned = clean_states(df_group_by_states)

    url_us_state_population = 'datasets/us-state-populations.csv'
    df_populations = read_csv(url_us_state_population)
    df_guns_and_population_merged = merge_datasets(df_states_cleaned, df_populations)
    df_merged_with_relatives = calculate_relative_values(df_guns_and_population_merged)
    analyze_kentucky(df_merged_with_relatives)

    print("\n---------- Ejercicio 6 ----------")
    url_us_state = "datasets/us-states.json"
    with open(url_us_state) as f:
        geo_data: json = json.load(f)

    map_permit_perc = create_choropleth_map(df_merged_with_relatives, geo_data, 'permit_perc', '% Permit')
    map_handgun_perc = create_choropleth_map(df_merged_with_relatives, geo_data, 'handgun_perc', '% Hand Guns')
    map_longgun_perc = create_choropleth_map(df_merged_with_relatives, geo_data, 'longgun_perc', '% Long Guns')

    # Las siguientes llamadas no funcionan quedan ejecutando hasta que se recive un timeout.
    # save_map_as_image(map_permit_perc, 'plots/map_permit_perc.png')
    # save_map_as_image(map_handgun_perc, 'plots/map_handgun_perc.png')
    # save_map_as_image(map_longgun_perc, 'plots/map_longgun_perc.png')
