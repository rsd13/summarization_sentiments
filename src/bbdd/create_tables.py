import sqlite3
import os


class BBDD:
    # formado por nombre,codProvincia,codigo

    def __init__(self, name="tripadvisor.db"):
        # ruta de la base de datos
        try:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            print(dir_path)
            self.bbdd = sqlite3.connect(dir_path + "/" + name, timeout=10)
            self.bbdd.row_factory = sqlite3.Row
            self.cursor = self.bbdd.cursor()
        except:
            raise("Error a conectar a la base de datos.")

    def create_tables(self):
        """
        crea todas las tablas automáticamente
        """

        self.create_local()
        self.create_reviews()
        self.create_local_reviews()

    def create_local(self):
        """
        crea la tabla local
        """

        query = """ CREATE TABLE IF NOT EXISTS local ( 
                        id integer PRIMARY KEY AUTOINCREMENT, 
                        nombre text NOT NULL
                    );"""

        self.exec_create_table(query, "local")

    def create_reviews(self):
        """
        crea la tabla reviews
        """

        query = """ CREATE TABLE IF NOT EXISTS reviews ( 
                        id integer PRIMARY KEY AUTOINCREMENT, 
                        comentario TEXT NOT NULL,
                        mes INTEGER NOT NULL,
                        año INTEGER NOT NULL
                        
                        
                    
                    );"""
        self.exec_create_table(query, "reviews")

    def create_local_reviews(self):
        """
        crea la table N:M entre local y reviews
        :return:
        """

        query = """ CREATE TABLE IF NOT EXISTS local_reviews ( 
                                id_reviews INTEGER NOT NULL,
                                id_local INTEGER NOT NULL,
                                PRIMARY KEY (id_reviews, id_local),
                                FOREIGN KEY(id_reviews) REFERENCES reviews(id),
                                FOREIGN KEY(id_local) REFERENCES local(id)

                            );"""

        self.exec_create_table(query, "local_reviews")


    def exec_create_table(self, query, name):
        """
        Ejecuta una query para crear una tabla cualquiera

        :param query: query para crear la tabla
        :param name: nombre de la tabla
        """

        try:
            self.cursor.execute(query)
        except NameError:
            raise("Error a crear la tabla {}: {}".format(name, NameError))
bbdd = BBDD()
bbdd.create_tables()
