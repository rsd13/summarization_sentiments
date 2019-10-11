from local import Local
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Supervisor(Local):
    """Clase que representa a un Supervisor"""

    def __init__(self, driver=webdriver.Firefox(), url=""):
        """Constructor de clase restaurante"""
        Local.__init__(self)
        self.driver = driver
        self.url = url


    def get_url(self):
        return self.url

    def create_drive(self):
        """
        función que crea el driver de Selenium para la conexión a una url
        :return:
        """
        try:
            self.driver.get(self.get_url())
        except ValueError:
            raise "Error a conectar con la url: {}".format(ValueError)
        return self


    def get_name_city_country(self):
        """
        función que crea el driver de Selenium para la conexión a una url
        :return:
        """
        name_restaurant = self.driver.find_element_by_css_selector("h1[class='header heading masthead masthead_h1 ']")
        name_restaurant, place_restaurant = name_restaurant.text.split(",")
        pais = self.driver.find_element_by_css_selector("span[class='country-name']").text

        self.nombre, self.ciudad, self.pais = name_restaurant, place_restaurant[1:], pais
        self.print_info_basic()

    def get_restaurante(self):
        """
        función que recoge la información del restaurante y sus reviews. Recogee
        el nombre, la ciudad, el país y los comentarios y los añade a la clase
        """
        self.create_drive()
        #consigo el nombre, pais y ciudad
        self.get_name_city_country()

url = "https://www.tripadvisor.es/Restaurant_Review-g1064230-d12741934-Reviews-or180-Goiko_Grill-Alicante_Costa_Blanca_Province_of_Alicante_Valencian_Country.html"

s = Supervisor(url=url)

s.get_restaurante()
