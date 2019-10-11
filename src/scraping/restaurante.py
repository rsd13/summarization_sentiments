from local import Local
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Restaurante(Local):
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

    def get_reviews(self, html):
        """
       función que deevuelve todas 10 reviews d eun restaurante
       """


        # recojo el grupo de reviews
        soup = BeautifulSoup(html, 'html.parser')
        group_reviews = soup.find("div", ["listContainer hide-more-mobile"])
        reviews = group_reviews.find_all("div", ["review-container"])

        #recojo todos los reviews junto a su fecha
        for review in reviews:
            try:
                dic = {}
                datas_reviews = review.find("div", ["ui_column is-9"])
                dic["texto"] = datas_reviews.find("p", ["partial_entry"]).text
                date = datas_reviews.find("div", ["prw_rup prw_reviews_stay_date_hsx"]).text
                dic["fecha"] = date.split(":")[1][1:]

                self.reviews.append(dic)
            except:
                raise("Error a recoger las reviews")


    def get_all_reviews(self):
        """
        función que deevuelve todas las reviews de un restaurante
        """
        while True:
            html = ""
            try:

                group_reviews = self.driver.find_elements_by_class_name("ulBlueLinks");

                try:
                    for group in group_reviews:
                        group.click()
                except:
                    print("Error, al dar click al comentario")
                    pass

                time.sleep(2)
                html = self.driver.page_source
                self.get_reviews(html)

                next = self.driver.find_element_by_css_selector("a[class='nav next taLnk ui_button primary']")
                time.sleep(1)
                next.click()

            # si no encuentra el boton salimos del bucle
            except:
                self.driver.close()
                break

    def get_restaurante(self):
        """
        función que recoge la información del restaurante y sus reviews. Recogee
        el nombre, la ciudad, el país y los comentarios y los añade a la clase
        """
        self.create_drive()
        #consigo el nombre, pais y ciudad
        self.get_name_city_country()
        #recojo las reviews
        self.get_all_reviews()


