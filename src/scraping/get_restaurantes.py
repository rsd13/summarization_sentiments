from scraping.restaurante import Restaurante
from bbdd.pais import Pais
from bbdd.ciudad import Ciudad
from bbdd.local import Local as BBDD_Local
from bbdd.reviews import Reviews
from bbdd.local_reviews import Local_reviews
import os


def get_restaurants(url):
    """
    dado una url devuelve la información de un restaurante de tripadvisor
    :param url: url del restaurante
    :return: el objeto restaurante con toda su informacióm
    """
    restaurante = Restaurante(url=url)
    restaurante.get_restaurante()
    return restaurante

def insert_datas(restaurante):
    """
    método que con la información del objeto restaurante lo introduce en la base de datos.
    """

    #inserto el pais
    Pais().insert_pais(restaurante.pais)
    Ciudad().insert_ciudad(restaurante.ciudad, restaurante.pais)
    BBDD_Local().insert_local(restaurante.nombre, restaurante.ciudad, restaurante.direccion, "restaurante")

    for i, review in enumerate(restaurante.reviews):
        if review["texto"] not in "Más...":
            Reviews().insert_reviews(review)
            Local_reviews().insert_local_reviews(review, restaurante.nombre, restaurante.ciudad, restaurante.direccion)



def save_restaurantes():
    dir_path = os.path.dirname(os.path.abspath(__file__)) + "/restaurantes.txt"
    f = open(dir_path, "r")
    lines = f.readlines()
    for line in lines:
        restaurante = get_restaurants(line)
        insert_datas(restaurante)

    restaurante.close_drive()








