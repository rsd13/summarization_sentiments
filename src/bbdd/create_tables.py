import sqlite3
import os


class BBDD:
    """
    Clase que administra la creación y la eliminación de tablas
    """
    # formado por nombre,codProvincia,codigo

    def __init__(self, name="tripadvisor.db"):
        # ruta de la base de datos
        """
        constructor donde se crea el cursor dee la base de datos. Para que funcione
        la base de datos tiene que estar en el mismo directorio del fichero.
        :param name: el nombre de la base de datos
        """
        try:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            self.bbdd = sqlite3.connect(dir_path + "/" + name, timeout=10)
            self.bbdd.row_factory = sqlite3.Row
            self.cursor = self.bbdd.cursor()
        except:
            raise("Error a conectar a la base de datos.")

    def drop_tables(self):
        """
        función que elimina todas las tablas
        """
        #el orden es al contrario al que se crea
        tables = ["local_reviews", "reviews", "local", "pais", "ciudad"]

        for table in tables:
            query = "drop table " + table
            try:
                self.cursor.execute(query)
            except NameError:
                raise ("Error a borrar la tabla {}: {}".format(table, NameError))


    def create_tables(self):
        """
        crea todas las tablas automáticamente
        """
        self.create_pais()
        self.create_ciudad()
        self.create_local()
        self.create_reviews()
        self.create_local_reviews()

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

    def create_local(self):
        """
        crea la tabla local
        """

        query = """ CREATE TABLE IF NOT EXISTS local ( 
                        id integer PRIMARY KEY AUTOINCREMENT, 
                        nombre text NOT NULL,
                        id_pais integer,
                        id_ciudad integer,
                        tipo text,
                        FOREIGN KEY(id_pais) REFERENCES pais(id),
                        FOREIGN KEY(id_ciudad) REFERENCES ciudad(id_ciudad),
                        constraint CK_TIPI check (tipo == "restaurante" or tipo == "hotel")
                        
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

    def create_pais(self):
        """
        crea la tabla pais
        """

        query = """ CREATE TABLE IF NOT EXISTS pais ( 
                                id INTEGER  PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT NOT NULL
                            );"""

        self.exec_create_table(query, "pais")

    def create_ciudad(self):
        """
         crea la tabla ciudad con restriccion de id a pais
        """

        query = """ CREATE TABLE IF NOT EXISTS ciudad ( 
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_pais INTEGER NOT NULL UNIQUE,
                                nombre TEXT NOT NULL,
                                FOREIGN KEY(id_pais) REFERENCES pais(id)
                            );"""

        self.exec_create_table(query, "ciudad")

def main():

    bbdd = BBDD()
    bbdd.create_tables()
    #bbdd.drop_tables()

if __name__ == '__main__':
    main()


