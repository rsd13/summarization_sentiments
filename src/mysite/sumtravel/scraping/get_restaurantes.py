from .restaurante  import Restaurante

def get_restaurants(url):
    """
    dado una url devuelve la información de un restaurante de tripadvisor
    :param url: url del restaurante
    :return: el objeto restaurante con toda su informacióm
    """
    restaurante = Restaurante(url=url)
    restaurante.get_restaurante()
    return restaurante


def save_restaurantes(url):

    restaurante = get_restaurants(url)
    return restaurante









