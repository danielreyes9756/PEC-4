import os
import unittest
import pandas as pd
from typing import Dict, List
from features.data_temporal_analysis import time_evolution


class TestDataTemporalAnalysis(unittest.TestCase):
    """
    Clase de testeo para las funcionalidades de data_temporal_analysis.
    """
    def setUp(self) -> None:
        """
        Función de configuración de datos para los tests de la clase data_temporal_analysis.
        :return: None
        """
        # Datos, para testear la funcionalidad de la clase data_temporal_analysis.
        data: Dict[str, List[object]] = {
            'year': [1998, 1999, 2000, 2001, 2002],
            'permit': [123, 455, 789, 134, 567],
            'handgun': [987, 654, 321, 211, 112],
            'longgun': [213, 754, 621, 111, 123],
        }

        # DataFrame para estudiar los cambiós provocados por data_temporal_analysis.
        self.df: pd.DataFrame = pd.DataFrame(data)

    def test_time_evolution(self) -> None:
        """
        Test para comprobar la función time_evolution.
        :return: None
        """
        # Act.
        try:
            time_evolution(self.df)

            # Asert.
            self.assertEqual(len(os.listdir("plots/")), 1), "No se creo el fichero png."
        except Exception as e:
            self.fail(f"test_time_evolution a fallado, se ha producido una excepción: {e}")


if __name__ == '__main__':
    unittest.main()
