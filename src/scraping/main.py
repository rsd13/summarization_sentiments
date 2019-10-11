from restaurante import Restaurante

def main():
    url = "https://www.tripadvisor.es/Restaurant_Review-g1064230-d12741934-Reviews-or180-Goiko_Grill-Alicante_Costa_Blanca_Province_of_Alicante_Valencian_Country.html"
    restaurante = Restaurante(url=url)
    restaurante.get_restaurante()



if __name__ == '__main__':
    main()
