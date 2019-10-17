from ..models import Review


def check_review(comentario, mes, anyo, local_id):
    """
    comprueba si existe una review en la bbddd para que no haya ducplicadas
    :param comentario: comentario del id
    :param mes: mes del id
    :param anyo: año del id
    :return:
    """
    review = Review.objects.filter(comentario=comentario, mes=mes, año=anyo, local_id=local_id)
    return review[0].id if len(review) > 0 else None

def insert_review(comentario, mes, anyo, local_id):
    """
    inserta una review en la base de datos
    :param comentario: comentario a inseretar
    :param mes: mes del comentario
    :param anyo: año del comentario
    :param anyo: id del local para insertarlo en la tabla many to many
    """

    #
    #si no existe el nombre del pais se inseerta
    id = check_review(comentario, mes, anyo, local_id)
    #si no existe, se inseerta
    if id == None:
        review =  Review.objects.create(comentario=comentario, mes=mes, año=anyo, local_id=local_id)
        review.save()




