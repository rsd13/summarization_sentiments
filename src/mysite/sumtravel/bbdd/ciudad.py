from ..models import Ciudad


def check_ciudad(nombre, pais_id):
    """
    indica si existe el pais
    :param nombre: nombre de la ciudad
    :param pais_id: id del pais
    :return: el id de la ciudad si existe, sino None
    """
    ciudad = Ciudad.objects.filter(nombre=nombre, pais_id=pais_id)
    return ciudad[0].id if len(ciudad) > 0 else None

def insert_ciudad(nombre, pais_id):
    """
    función que inserta un pais en la base de datos
    :param nombre: nombre del pais
    return: el id del pais
    """
    #
    #si no existe el nombre del pais se inseerta
    id = check_ciudad(nombre, pais_id)
    #si no existe, se inseerta
    if id == None:
        ciudad = Ciudad.objects.create(nombre=nombre, pais_id=pais_id)
        ciudad.save()
        return ciudad.id

    return id


