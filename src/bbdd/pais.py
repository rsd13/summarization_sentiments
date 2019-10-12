
import sqlite3
import os

class Pais:

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

    #metidis de insertar
    def insert_pais(self, pais):
        """
        inserta el pais en la base de datos, primero se comprueba si existe para insertarlo
        :param pais: nombre del pais a insertar
        """
        # comprobamos si existe
        self.cursor.execute("select * " +
                            "from pais " +
                            "where nombre=?", (
                                pais,
                            ))

        lineas = self.cursor.fetchall()
        # si no existe esa fecha se inserta
        if len(lineas) == 0:

            self.cursor.execute("INSERT INTO pais(nombre) VALUES (?)", (pais, ))
            self.bbdd.commit()


    def get_id(self, nombre):
        """
        dado un nombre de pais que recoja el id
        :param nombre: el nombre de pais a buscar
        """
        self.cursor.execute("""
                                SELECT id
                                FROM pais 
                                WHERE nombre=?""", (nombre,))
        id = self.cursor.fetchone()[0]
        return id


