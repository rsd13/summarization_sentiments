from ..models import Pais


def check_pais(nombre):
    """
    funcion quee comprueba si existe el nombre del pais
    :param nombre: nombre del pais
    :return: id si existee, sino None
    """
    pais = Pais.objects.filter(nombre=nombre)
    return pais[0].id if len(pais) > 0 else None

def insert_Pais(nombre):
    """
    función que inserta un pais en la base de datos
    :param nombre: nombre del pais
    return: el id del pais
    """


    #si no existe el nombre del pais se inseerta
    id = check_pais(nombre)
    #si no existe, se inseert
    if id == None:
        pais = Pais.objects.create(nombre=nombre)
        pais.save()
        return pais.id

    return id


