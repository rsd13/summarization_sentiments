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
from .summarization.summarization import get_sum
import spacy

NLP = spacy.load('es_core_news_sm')

def index(request):

    return render(request, 'sumtravel/index.html')


def get_restaurant(request):
    context = ""
    try:
        nombre, ciudad = request.GET.get("nombre"), request.GET.get("ciudad")
        id_ciudad = Ciudad.objects.filter(nombre__contains=ciudad)[0].id
        local = Local.objects.filter(nombre__contains=nombre, ciudad_id=id_ciudad)
        print("localees")
        print(local)

        context = {
            "restaurantes": local
        }

        return render(request, 'sumtravel/get_restaurant.html', context)
    except:
        return render(request, 'sumtravel/get_restaurant.html', context)

def restaurant(request, restaurante_id):
    reviews = Review.objects.filter(local_id=restaurante_id)
    local = Local.objects.filter(id=restaurante_id)
    #obtengo el texto resumido con la información de las gráficas
    lst = get_sum(restaurante_id, NLP, local[0].dirección)

    anyos = [review.año for review in reviews]

    context = {
        "reviews": reviews,
        "restaurante": local[0],
        "grafica_positiva": lst,
        "años": set(anyos)
    }
    return render(request, 'sumtravel/restaurant.html',context)

def insert_restaurant(request):
    return render(request, 'sumtravel/insert_restaurant.html')

#insereta los restaurantes
def insert_restaurant_database(request):

    try:
        #obtengo la información de los restaurantes

        url = request.GET.get("url")
        restaurante = save_restaurantes(url)
        restaurante.print_info_basic()

        #inserta el pais, la ciudad y el local
        pais_id = insert_Pais(restaurante.pais)
        ciudad_id = insert_ciudad(restaurante.ciudad, pais_id)
        local_id = insert_local(restaurante.nombre, restaurante.direccion, ciudad_id, restaurante.foto)

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

