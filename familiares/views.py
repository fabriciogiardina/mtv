from django.shortcuts import render
from django.http import HttpResponse
from .models import familiar
from django.template import Template, Context, loader

# Create your views here.

def guardarMostrarFamiliares (request):
    familiar1 = familiar (nombre="Nazira", edad= 7, fecha_nacimiento= "2015-02-23")
    familiar2 = familiar (nombre="Giovanni", edad= 0, fecha_nacimiento= "2022-06-16")
    familiar3 = familiar (nombre="Valeria", edad= 36, fecha_nacimiento= "1986-08-20")

    familiar1.save()
    familiar2.save()
    familiar3.save()

    familiares = {familiar1, familiar2, familiar3}

    lista_familia = {"familiares": familiares}

    template = loader.get_template("familiares.html")

    documento = template.render(lista_familia)
    return HttpResponse (documento)

    