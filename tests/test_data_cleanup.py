import unittest
from typing import Dict, List
import pandas as pd
from features.data_cleanup import read_csv, clean_csv, rename_col


class TestDataCleanup(unittest.TestCase):
    """
    Clase de testeo para las funcionalidades de data_cleanup.
    """
    def setUp(self) -> None:
        """
        Función de configuración de datos para los tests de la clase data_cleanup.
        :return: None
        """
        # Datos, para testear la funcionalidad de la clase data_cleanup.
        data: Dict[str, List[object]] = {
            'month': ['2020-01', '2023-02'],
            'state': ['Alabama', 'Dakota'],
            'permit': [1000, 200],
            'handgun': [10, 23],
            'long_gun': [132, 51],
            'other': [4, 6]
        }

        # DataFrame para estudiar los cambiós provocados por data_clenaup.
        self.df: pd.DataFrame = pd.DataFrame(data)

        # Ruta para testear la función read_csv de data_cleanup.
        self.path: str = '../datasets/nics-firearm-background-checks.csv'

    def test_read_csv(self) -> None:
        """
        Test para la función test_read_csv de la clase data_cleanup.
        :return: None
        """
        # Arrange.
        df: pd.DataFrame = None

        # Precodition.
        self.assertIsNone(df), "El DataFrame debería estar inicializado a None."

        # Act.
        df = read_csv(self.path)

        # Assert.
        self.assertIsNotNone(df), "El DataFrame debería contener información."

    def test_clean_csv(self) -> None:
        """
        Test para comprobar la función clean_csv.
        :return: None
        """
        expected_columns: List[str] = ['month', 'state', 'permit', 'handgun', 'long_gun']
        df_cleaned: pd.DataFrame = clean_csv(self.df)
        self.assertListEqual(list(df_cleaned.columns), expected_columns), "La columna 'other' no se elimino."

    def test_rename_col(self) -> None:
        """
        Test para comprobar la función rename_col.
        :return: None
        """
        expected_columns: List[str] = ['month', 'state', 'permit', 'handgun', 'longgun', 'other']

        # Test cuando se encuentra la columna long_gun, (long_gun debe de ser sustituido).
        df_renamed: pd.DataFrame = rename_col(self.df)
        self.assertListEqual(list(df_renamed.columns), expected_columns), "La columna 'long_gun' no se renombro."

        # Test cuando no se encuentra la columna long_gun, (no deben suceder cambios).
        df_renamed: pd.DataFrame = rename_col(df_renamed)
        self.assertListEqual(list(df_renamed.columns), expected_columns), "Se ha producido un cambio no esperado."


if __name__ == '__main__':
    unittest.main()
