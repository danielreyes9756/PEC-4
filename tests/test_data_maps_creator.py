import json
import folium
import unittest
import pandas as pd
from typing import Dict, List
from features.data_maps_creator import create_choropleth_map


class TestDataMapsCreator(unittest.TestCase):
    """
    Clase de testeo para las funcionalidades de data_maps_creator.
    """
    def setUp(self) -> None:
        """
        Función de configuración de datos para los tests de la clase data_maps_creator.
        :return: None
        """
        # Datos, para testear la funcionalidad de la clase data_maps_creator.
        data: Dict[str, List[object]] = {
            'state':  ['Alabama'],
            'permit': [2302302],
            'handgun': [3007],
            'longun': [3232323232],
            'permit_perc': [53.157797],
            'handgun_perc': [37.772007],
            'longun_perc': [59.917697]
        }

        # DataFrame para estudiar los cambiós provocados por data_maps_creator.
        self.df: pd.DataFrame = pd.DataFrame(data)

        url_us_state: str = "../datasets/us-states.json"
        with open(url_us_state) as f:
            self.geo_data: json = json.load(f)

    def test_create_choropleth_map(self) -> None:
        """
        Test para la función create_choropleth_map de la clase data_maps_creator.
        :return: None
        """
        # Arrange.
        permit_map: folium.Map = None

        # Precodition.
        self.assertIsNone(permit_map), "El mapa debe estar vacio inicialmente."

        # Act.
        permit_map = create_choropleth_map(self.df, self.geo_data, 'permit_perc', '% Permit')

        # Assert.
        self.assertIsNotNone(permit_map), "El mapa no se creo correctamente."


if __name__ == '__main__':
    unittest.main()
