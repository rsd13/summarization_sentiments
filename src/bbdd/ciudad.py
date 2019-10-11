

class Ciudad:

    def __init__(self):
        self.nombre = None
        self.pais = None
        self.ciudad = None
        self.reviews = []

    def print_info_basic(self):
        """función que imprime el nombre, ciudad y pais"""
        print("Restaurante: {} en {}, {}".format(self.nombre,self.ciudad,self.pais))
