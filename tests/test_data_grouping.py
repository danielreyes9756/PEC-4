import unittest
from typing import Dict, List
import pandas as pd
from features.data_grouping import group_by_state_and_year, print_biggest_handguns, print_biggest_longguns


class TestDataGrouping(unittest.TestCase):
    """
    Clase de testeo para las funcionalidades de data_grouping.
    """
    def setUp(self) -> None:
        """
        Función de configuración de datos para los tests de la clase data_grouping.
        :return: None
        """
        # Datos, para testear la funcionalidad de la clase data_grouping.
        data: Dict[str, List[object]] = {
            'year': [2021, 2021, 2023, 2023, 2023, 2024],
            'state': ['Alabama', 'Alaska', 'Alabama', 'Dakota', 'Dakota', 'Alaska'],
            'permit': [1000, 200, 300, 1200, 11, 255],
            'handgun': [10, 23, 35, 55, 311, 54],
            'longgun': [132, 51, 12, 23, 25, 62],
        }

        # DataFrame para estudiar los cambiós provocados por data_grouping.
        self.df: pd.DataFrame = pd.DataFrame(data)

    def test_group_by_state_and_year(self) -> None:
        """
        Test para comprobar la función group_by_state_and_year.
        :return: None
        """
        # Arrange.
        expected_shape: (int, int) = (5, 5)
        expected_data: Dict[str, List[object]] = {
            'year': [2021, 2021, 2023, 2023, 2024],
            'state': ['Alabama', 'Alaska', 'Alabama', 'Dakota', 'Alaska'],
            'permit': [1000, 200, 300, 1211, 255],
            'handgun': [10, 23, 35, 366, 54],
            'longgun': [132, 51, 12, 48, 62],
        }
        expected_df: pd.DataFrame = pd.DataFrame(expected_data)

        # Precondition.
        self.assertNotEqual(self.df.shape, expected_shape), f"La agrupación inicial debería contar con una" \
                                                            f" forma diferente a la siguiente {expected_shape}."

        # Act.
        df_grouped: pd.DataFrame = group_by_state_and_year(self.df)

        # Assert.
        self.assertEqual(df_grouped.shape, expected_shape), "La agrupación no se ha producido correctamente."
        pd.testing.assert_frame_equal(df_grouped, expected_df), "No se han hecho las módificaciones pertinentes."

    def test_print_biggest_handguns(self) -> None:
        """
        Test para comprobar la función print_biggest_handguns.
        :return: None
        """
        # Arrange.
        df_grouped: pd.DataFrame = group_by_state_and_year(self.df)

        # Act.
        print_biggest_handguns(df_grouped)

        # Assert.
        print("print_biggest_handguns no se puede testear, pero se puede observar su correcta ejecución")

    def test_print_biggest_longguns(self) -> None:
        """
        Test para comprobar la función print_biggest_longguns.
        :return: None
        """
        # Arrange.
        df_grouped: pd.DataFrame = group_by_state_and_year(self.df)

        # Act.
        print_biggest_longguns(df_grouped)

        # Assert.
        print("print_biggest_longguns no se puede testear, pero se puede observar su correcta ejecución")


if __name__ == '__main__':
    unittest.main()
