import unittest
import pandas as pd
from typing import Dict, List
from features.data_status_analysis import groupby_state,\
    clean_states,\
    merge_datasets,\
    calculate_relative_values,\
    analyze_kentucky


class TestDataStatusAnalysis(unittest.TestCase):
    """
    Clase de testeo para las funcionalidades de data_status_analysis.
    """
    def setUp(self) -> None:
        """
        Función de configuración de datos para los tests de la clase data_status_analysis.
        :return: None
        """
        # Datos sobre armas, para testear la funcionalidad de la clase data_temporal_analysis.
        guns_data: Dict[str, List[object]] = {
            'year': [2021, 2021, 2023, 2023, 2023, 2024, 2024, 2024, 2024, 2024],
            'state': [
                'Alabama', 'Alaska', 'Alabama',
                'Dakota', 'Dakota', 'Alaska',
                'Guam', 'Puerto Rico', 'Virginia Islands',
                'Kentucky'],
            'permit': [1000, 200, 300, 1200, 11, 255, 102, 103, 104, 123232],
            'handgun': [10, 23, 35, 55, 311, 54, 107, 106, 105, 220220],
            'longgun': [132, 51, 12, 23, 25, 62, 112, 113, 114, 230230]
        }

        # DataFrame de armas para estudiar los cambiós provocados por data_status_analysis.
        self.df_guns: pd.DataFrame = pd.DataFrame(guns_data)

        # Datos sobre la población, para testear la funcionalidad de la clase data_status_analysis.
        data_population: Dict[str, List[object]] = {
            'state': ['Alabama', 'Alaska', 'Dakota', 'Kentucky'],
            'pop_2014': [93923929, 2023010, 173272, 1293239]
        }

        # DataFrame poblacional para estudiar los cambiós provocados por data_status_analysis.
        self.df_population: pd.DataFrame = pd.DataFrame(data_population)

    def test_groupby_state(self) -> None:
        """
        Test para comprobar la función groupby_state.
        :return: None
        """
        # Arrange.
        expected_data: Dict[str, List[object]] = {
            'state': ['Alabama', 'Alaska', 'Dakota', 'Guam', 'Kentucky', 'Puerto Rico', 'Virginia Islands'],
            'permit': [1300, 455, 1211, 102, 123232, 103, 104],
            'handgun': [45, 77, 366, 107, 220220, 106, 105],
            'longgun': [144, 113, 48, 112, 230230, 113, 114]
        }
        expected_df: pd.DataFrame = pd.DataFrame(expected_data)

        # Act.
        df_group_by_states: pd.DataFrame = groupby_state(self.df_guns)

        # Assert.
        pd.testing.assert_frame_equal(df_group_by_states, expected_df), "La módificación realizada es incorrecta."

    def test_clean_states(self) -> None:
        """
        Test para comprobar la función clean_states.
        :return: None
        """
        # Arrange.
        expected_data: Dict[str, List[object]] = {
            'state': ['Alabama', 'Alaska', 'Dakota', 'Kentucky'],
            'permit': [1300, 455, 1211, 123232],
            'handgun': [45, 77, 366, 220220],
            'longgun': [144, 113, 48, 230230]
        }
        expected_df: pd.DataFrame = pd.DataFrame(expected_data)
        df_group_by_states: pd.DataFrame = groupby_state(self.df_guns)

        # Act.
        df_states_cleaned: pd.DataFrame = clean_states(df_group_by_states)

        # Assert.
        self.assertNotIn('Guam', df_states_cleaned), "No se elimino el estado Gaum."
        self.assertNotIn('Puerto Rico', df_states_cleaned), "No se elimino el estado Puerto Rico."
        self.assertNotIn('Virginia Islands', df_states_cleaned), "No se elimino el estado Virginia Islands."
        pd.testing.assert_frame_equal(df_states_cleaned, expected_df), "Se han realizado cambios inesperados."

    def test_merge_datasets(self) -> None:
        """
        Test para comprobar la función merge_datasets.
        :return: None
        """
        # Arrange.
        expected_data: Dict[str, List[object]] = {
            'state': ['Alabama', 'Alaska', 'Dakota', 'Kentucky'],
            'permit': [1300, 455, 1211, 123232],
            'handgun': [45, 77, 366, 220220],
            'longgun': [144, 113, 48, 230230],
            'pop_2014': [93923929, 2023010, 173272, 1293239]
        }
        expected_df: pd.DataFrame = pd.DataFrame(expected_data)
        df_group_by_states: pd.DataFrame = groupby_state(self.df_guns)
        df_states_cleaned: pd.DataFrame = clean_states(df_group_by_states)

        # Act.
        df_merged: pd.DataFrame = merge_datasets(df_states_cleaned, self.df_population)

        # Assert.
        pd.testing.assert_frame_equal(df_merged, expected_df), "Se han realizado correctamente la unión de DataFrames."

    def test_calculate_relative_values(self) -> None:
        """
        Test para comprobar la función calculate_relative_values.
        :return: None
        """
        # Arrange.
        expected_data: Dict[str, List[object]] = {
            'state': ['Alabama', 'Alaska', 'Dakota', 'Kentucky'],
            'permit': [1300, 455, 1211, 123232],
            'handgun': [45, 77, 366, 220220],
            'longgun': [144, 113, 48, 230230],
            'pop_2014': [93923929, 2023010, 173272, 1293239],
            'permit_perc': [0.0013840988274670665, 0.0224912383033203, 0.6989011496375641, 9.528942446059855],
            'longgun_perc': [0.0001533155624271212, 0.005585736106099327, 0.02770210997737661, 17.80258714746462],
            'handgun_perc': [4.7911113258475375e-05, 0.0038062095590234352, 0.21122858857749666, 17.028561619313987],
        }
        expected_df: pd.DataFrame = pd.DataFrame(expected_data)
        df_group_by_states: pd.DataFrame = groupby_state(self.df_guns)
        df_states_cleaned: pd.DataFrame = clean_states(df_group_by_states)
        df_merged: pd.DataFrame = merge_datasets(df_states_cleaned, self.df_population)

        # Act.
        df_with_relatives: pd.DataFrame = calculate_relative_values(df_merged)

        # Assert.
        pd.testing.assert_frame_equal(df_with_relatives, expected_df), "Se han producido un error al intentar" \
                                                                       "unir los DataFrames de armas y población."

    def test_analyze_kentucky(self) -> None:
        """
        Test para comprobar la función analyze_kentucky.
        :return: None
        """
        # Arrange.
        df_group_by_states: pd.DataFrame = groupby_state(self.df_guns)
        df_states_cleaned: pd.DataFrame = clean_states(df_group_by_states)
        df_merged: pd.DataFrame = merge_datasets(df_states_cleaned, self.df_population)
        df_with_relatives: pd.DataFrame = calculate_relative_values(df_merged)

        # Act.
        analyze_kentucky(df_with_relatives)

        # Assert.
        print("No puede ser testeado, pero podemos observar su correcta ejecución")


if __name__ == '__main__':
    unittest.main()
