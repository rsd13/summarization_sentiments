from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the sumtravel index.")

def pais(request, pais_id):
    return HttpResponse("You're looking at question %s." % pais_id)
