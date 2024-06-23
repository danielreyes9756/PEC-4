import unittest
from typing import Dict, List
import pandas as pd
from features.data_processing import breakdown_date, erase_month


class TestDataProcessing(unittest.TestCase):
    """
    Clase de testeo para las funcionalidades de data_processing.
    """
    def setUp(self) -> None:
        """
        Función de configuración de datos para los tests de la clase data_processing.
        :return: None
        """
        # Datos, para testear la funcionalidad de la clase data_processing.
        data: Dict[str, List[object]] = {
            'month': ['2021-01', '2022-03'],
            'state': ['Alabama', 'Alaska'],
            'permit': [1000, 200],
            'handgun': [10, 2354],
            'longgun': [132, 5125],
        }

        # DataFrame para estudiar los cambiós provocados por data_processing.
        self.df: pd.DataFrame = pd.DataFrame(data)

    def test_breakdown_date(self) -> None:
        """
        Test para comprobar la función breakdown_date.
        :return: None
        """
        # Arrange.
        expected_data: Dict[str, List[object]] = {
            'month': [1, 3],
            'state': ['Alabama', 'Alaska'],
            'permit': [1000, 200],
            'handgun': [10, 2354],
            'longgun': [132, 5125],
            'year': [2021, 2022]
        }
        expected_df: pd.DataFrame = pd.DataFrame(expected_data)
        expected_shape: (int, int) = expected_df.shape

        # Precondition.
        self.assertNotEqual(self.df.shape, expected_shape), f"El DataFrame inicial debería contar con una" \
                                                            f" forma diferente a la siguiente {expected_shape}."
        self.assertTrue('year' not in self.df.columns), f"La columna 'year' no se encuentra originalmente" \
                                                        " en el DataFrame"

        # Act.
        df_breakdown_date: pd.DataFrame = breakdown_date(self.df)

        # Assert.
        self.assertEqual(df_breakdown_date.shape, expected_shape), "La división de datos no se ha producido."
        pd.testing.assert_frame_equal(df_breakdown_date, expected_df), "No se han hecho las módificaciones pertinentes."
        self.assertTrue('year' in df_breakdown_date.columns), "La columna 'year' no se agrego al DataFrame a partir" \
                                                              "de dividir la columna month"

    def test_erase_month(self) -> None:
        """
        Test para comprobar la función breakdown_date.
        :return: None
        """
        # Arrange.
        expected_data: Dict[str, List[object]] = {
            'state': ['Alabama', 'Alaska'],
            'permit': [1000, 200],
            'handgun': [10, 2354],
            'longgun': [132, 5125],
            'year': [2021, 2022]
        }
        expected_df: pd.DataFrame = pd.DataFrame(expected_data)
        df_breakdown_date: pd.DataFrame = breakdown_date(self.df)

        # Precondition.
        self.assertTrue('month' in self.df.columns), f"La columna 'month' se debería encontrar en el DataFrame."

        # Act.
        df_month_erased: pd.DataFrame = erase_month(df_breakdown_date)

        # Assert.
        pd.testing.assert_frame_equal(df_month_erased, expected_df), "No se han hecho las módificaciones pertinentes."
        self.assertTrue('month' not in df_month_erased.columns), "La columna 'month' no se elimino del DataFrame."


if __name__ == '__main__':
    unittest.main()
