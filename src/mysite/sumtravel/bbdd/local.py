from ..models import Local


def check_local(nombre, direccion, ciudad_id):
    """
    indica si existe un local
    :param nombre: nombre del local
    :param direccion: dirección del local
    :param ciudad_id: ciudad del local
    :return: id del local si existe, sino Nonee
    """
    local = Local.objects.filter(nombre=nombre, dirección=direccion,
                                 tipo="restaurante", ciudad_id=ciudad_id)

    return local[0].id if len(local) > 0 else None

def insert_local(nombre, direccion, ciudad_id, foto):
    """
    inserta un local en la base de datos
    :param nombre: nombre del local
    :param direccion: dirección del local
    :param ciudad_id: id de la ciudad del local
    :return: id del local
    """
    #
    #si no existe el nombre del pais se inseerta
    id = check_local(nombre, direccion, ciudad_id)
    #si no existe, se inseerta
    if id == None:
        local = Local.objects.create(nombre=nombre, dirección=direccion,
                                    tipo="restaurante",img=foto, ciudad_id=ciudad_id)
        local.save()
        return local.id

    return id


