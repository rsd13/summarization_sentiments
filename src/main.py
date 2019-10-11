from scraping.restaurante import Restaurante
import bbdd.pais
from bbdd.ciudad import Ciudad
from bbdd.local import Local as BBDD_Local


def get_restaurants(url):
    """
    dado una url devuelve la información de un restaurante de tripadvisor
    :param url: url del restaurante
    :return: el objeto restaurante con toda su informacióm
    """
    url = "https://www.tripadvisor.es/Restaurant_Review-g1064230-d12741934-Reviews-or180-Goiko_Grill-Alicante_Costa_Blanca_Province_of_Alicante_Valencian_Country.html"
    restaurante = Restaurante(url=url)
    restaurante.get_restaurante()
    return restaurante


def insert_datas(restaurante):
    """
    método que con la información del objeto restaurante lo introduce en la base de datos.
    """

    #inserto el pais
    bbdd.pais.Pais().insert_pais(restaurante.pais)
    Ciudad().insert_ciudad(restaurante.ciudad, restaurante.pais)
    BBDD_Local().insert_local(restaurante.nombre, restaurante.ciudad, restaurante.direccion, "restaurante")

def main():
    restaurante = get_restaurants("")

    #inserto los datos
    insert_datas(restaurante)



if __name__ == '__main__':

    main()



