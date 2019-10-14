from django.shortcuts import render
from .models import Ciudad
from .models import Local
from .models import Review
from .models import Pais
from .scraping.get_restaurantes import save_restaurantes
from .bbdd.pais import insert_Pais
from .bbdd.ciudad import insert_ciudad
from .bbdd.local import insert_local
from .bbdd.reviews import insert_review


def email_check(user):
    return user.email.endswith('@example.com')


def index(request):
    return render(request, 'sumtravel/index.html')


"""def get_restaurant(request):
    pass
"""
def insert_restaurant(request):
    return render(request, 'sumtravel/insert_restaurant.html')

#insereta los restaurantes
def insert_restaurant_database(request):
    print("SDFSDFSSFD")
    try:
        #obtengo la información de los restaurantes
        url = request.GET.get("url")
        restaurante = save_restaurantes(url)
        restaurante.print_info_basic()

        #inserta el pais, la ciudad y el local
        pais_id = insert_Pais(restaurante.pais)
        ciudad_id = insert_ciudad(restaurante.ciudad, pais_id)
        local_id = insert_local(restaurante.nombre, restaurante.direccion, ciudad_id)

        for review in restaurante.reviews:
            #por si no ha hecho bien el scrapeo
            if review["texto"] not in "Más...":
                comentario, mes, anyo = review["texto"], review["mes"], review["año"]
                insert_review(comentario, mes, anyo, local_id)


        context = {
            "alert": False
        }
        return render(request, 'sumtravel/insert.html', context)

    except:

        context = {
            "alert": True
        }
        return render(request, 'sumtravel/insert.html', context)

