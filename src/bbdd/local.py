
import sqlite3
import os
from bbdd.ciudad import Ciudad

class Local:

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
    def insert_local(self, nombre, ciudad, direccion, tipo):
        """
        inserta el local en la base de datos
        :param nombre: nombre del local
        :param ciudad: ciudad del local
        :return:
        """
        
        # busco el id de la ciudad
        id_ciudad = Ciudad().get_id(ciudad)

        rows = self.check_local(nombre, id_ciudad, direccion)

        #si no existe lo introducimos
        if len(rows) == 0:
            self.cursor.execute("INSERT INTO local(nombre, id_ciudad,direccion,tipo) "
                                "VALUES (?,?,?,?)", (nombre,id_ciudad, direccion, tipo,))
            self.bbdd.commit()




        #busco el si existe por nombre y por dirección


    def check_local(self, nombre, ciudad, direccion):
        """
        función que comprueba si existe un local en una base de datos
        :param nombre: nombre del local
        :param ciudad: nombre de la ciudad de del local
        :param direccion: nombre de la dirección del local
        :return:
        """

        self.cursor.execute("""
                                SELECT id
                                FROM local 
                                WHERE nombre=? and id_ciudad=? and direccion= ?
                                
                                """, (nombre,ciudad, direccion))

        return self.cursor.fetchall()


