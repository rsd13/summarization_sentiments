import sqlite3
import os
from bbdd.pais import Pais

class Ciudad:

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
    def insert_ciudad(self, ciudad, pais):
        """
        inserta la ciudad en la base de datos, primero se comprueba si existe para insertarlo
        :param pais: nombre del pais a insertar
        """

        # comprobamos si existe
        self.cursor.execute("""
                            select * 
                            from ciudad 
                            where nombre=? """, (
                                ciudad,))


        rows = self.cursor.fetchall()
        # si no existe esa fecha se inserta

        if len(rows) == 0:

            #primero obtengo el pais (como se inserta primero el pais no hace falta comprobar si existe)

            id = Pais().get_id(pais)
            self.cursor.execute("INSERT INTO ciudad(id_pais, nombre) VALUES(?,?)", (id, ciudad))
            self.bbdd.commit()

    def get_id(self, nombre):
        """
        dado un nombre de ciudad y pais recoje el id
        :param nombre: el nombre de pais a buscar
        """
        print(nombre)
        self.cursor.execute("""
                                SELECT id
                                FROM ciudad 
                                WHERE nombre=?""", (nombre,))

        row = self.cursor.fetchone()
        if len(row) == 0:
            return None
        id = row[0]
        return id




