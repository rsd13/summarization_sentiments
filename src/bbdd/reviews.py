import sqlite3
import os


class Reviews:

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
    def insert_reviews(self, review):

        """
        inseera reviews en la base de datos
        :param comentario: información del review
        """
        comentario, mes, año = review["texto"], review["mes"], review["año"]
        rows = self.check_review(comentario, mes, año)
        print(comentario)
        # si no existe lo introducimos
        if len(rows) == 0:
            self.cursor.execute("INSERT INTO reviews(comentario, mes, año) "
                                "VALUES (?,?,?)", (comentario, mes, año,))
            self.bbdd.commit()

        # busco el si existe por nombre y por dirección

    def check_review(self, comentario, mes, año):
        """
        función que comprueba si existe una review e
        :param comentario: nombre del local
        :param mes: nombre de la ciudad de del local
        :param año: nombre de la dirección del local
        :return:
        """

        self.cursor.execute("""
                                SELECT id
                                FROM reviews
                                WHERE comentario=? and mes=? and año= ?

                                """, (comentario, mes, año))
        rows = self.cursor.fetchall()
        return rows




