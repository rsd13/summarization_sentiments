from selenium import webdriver

class Local:

    def __init__(self, driver=webdriver.Firefox()):
        self.nombre = None
        self.pais = None
        self.ciudad = None
        self.direccion = None
        self.reviews = []
        self.driver = driver

    def print_info_basic(self):
        """función que imprime el nombre, ciudad y pais"""
        print("Restaurante: {} en {}, {}, {}".format(self.nombre, self.ciudad,self.direccion, self.pais))



    def close_drive(self):
        """
        función que cierra el drive
        """
        self.driver.close()


