from django.shortcuts import render
from .models import Ciudad
from .models import Local
from .models import Review
from .models import Pais
from django.http import Http404
from .scraping.get_restaurantes import save_restaurantes



"""def index(request):
    return HttpResponse("Hello, world. You're at the sumtravel index.")"""

def get_restaurant(request):

    return render(request, 'sumtravel/get_restaurant.html')

def index(request):
    latest_question_list = Pais.objects.order_by("nombre")
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'sumtravel/index.html', context)


#insereta los restaurantes
def insert_restaurant(request):

    url = request.GET.get("url")
    restaurante = save_restaurantes(url)
    restaurante.print_info_basic()
    return render(request, 'sumtravel/insert.html')

