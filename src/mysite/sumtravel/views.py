from django.shortcuts import render
from .models import Ciudad
from .models import Local
from .models import Review
from .models import Pais
from django.http import Http404
from .scraping.get_restaurantes import save_restaurantes
from django.contrib.auth.decorators import user_passes_test

def email_check(user):
    return user.email.endswith('@example.com')


"""def index(request):
    return HttpResponse("Hello, world. You're at the sumtravel index.")"""

from django.contrib.auth.decorators import login_required, permission_required

def get_restaurant(request):
    print(email_check)
    return render(request, 'sumtravel/get_restaurant.html')

def index(request):
    print(request)
    latest_question_list = Pais.objects.order_by("nombre")
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'sumtravel/index.html', context)


#insereta los restaurantes
def insert_restaurant(request):

    #try:
    url = request.GET.get("url")
    restaurante = save_restaurantes(url)
    restaurante.print_info_basic()
    print("Empiezo pais")
    pais = Pais.objects.create(nombre=restaurante.pais)
    pais.save()
    print("Empiezo ciudad")
    print(pais.id)
    ciudad = Ciudad.objects.create(nombre=restaurante.ciudad, pais_id=pais.id)
    ciudad.save()
    print("Empiezo local",ciudad.id)
    local = Local.objects.create(nombre=restaurante.nombre, dirección=restaurante.direccion,
                                tipo="restaurante", ciudad_id=ciudad.id)
    local.save()
    print("empiezo reviews")
    for review in restaurante.reviews:
        #por si no ha hecho bien el scrapeo
        if review["texto"] not in "Más...":
            comentario, mes, anyo = review["texto"], review["mes"], review["año"]
            print(comentario, mes, anyo)
            review_instance = Review.objects.create(comentario=comentario, mes=mes, año=anyo)
            review_instance.save()
            review_instance.local.add(local.id)

    print("terminado!")
    context = {
        "alert": False
    }
    return render(request, 'sumtravel/insert.html', context)

    """except:
        print("ERRROR")
        context = {
            "alert": True
        }
        return render(request, 'sumtravel/insert.html', context)"""

