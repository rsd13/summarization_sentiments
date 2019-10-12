import sqlite3
import os
from bbdd.local import Local
from bbdd.reviews import Reviews
from bbdd.ciudad import Ciudad


class Local_reviews:

    def __init__(self, name="tripadvisor.db"):
        # ruta de la base de datos
        """
        constructor de Pais que contiene las funciones de pais( CRUD)
        """
        try:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            self.bbdd = sqlite3.connect(dir_path + "/" + name, timeout=10)
            self.bbdd.row_factory = sqlite3.Row
            self.cursor = self.bbdd.cursor()
        except:
            raise ("Error a conectar la base de datos")

    # metidis de insertar
    def insert_local_reviews(self, review, nombre, ciudad, direccion):

        """
        interta la relación entre locales y reviews
        :param comentario: información del review
        """
        comentario, mes, año = review["texto"], review["mes"], review["año"]
        id_ciudad = Ciudad().get_id(ciudad)
        id_local = Local().check_local(nombre, id_ciudad, direccion)
        id_review = Reviews().check_review(comentario, mes, año)


        # busco el si existe por nombre y por dirección

        row = self.check_local(id_local[0][0], id_review[0][0])

        if len(row) == 0:
            self.cursor.execute("INSERT INTO local_reviews(id_reviews, id_local) "
                                "VALUES (?,?)", (id_review[0][0], id_local[0][0], ))
            self.bbdd.commit()


    def check_local(self, local, review):

        print(local, review)

        self.cursor.execute("""
                                SELECT *
                                FROM local_reviews 
                                WHERE id_reviews=? and id_local=? 
                                """, (review, local, ))

        rows = self.cursor.fetchall()
        return rows
