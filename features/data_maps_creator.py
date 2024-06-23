import io
import json
import folium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from PIL import Image


def create_choropleth_map(data, json_data: json, column, title) -> folium.Map:
    folium_map: folium.Map = folium.Map(lcation=[37.8, -96], zoom_start=4)

    folium.Choropleth(
        geo_data=json_data,
        name="x",
        data=data,
        columns=["state", column],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=title
    ).add_to(folium_map)

    folium.LayerControl().add_to(folium_map)

    return folium_map


def save_map_as_image(folium_map: folium.Map, filename: str):
    folium_map.save("temp_map.html")

    options: Options = Options()
    options.add_argument('--headless')
    service: Service = Service(executable_path=GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service, options=options)

    browser.get("file://" + "plot/temp_map.html")
    img_date = browser.get_screenshot_as_png()
    browser.quit()

    img = Image.open(io.BytesIO(img_date))
    img.save(filename)
