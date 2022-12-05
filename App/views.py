from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader 
import datetime

# Create your views here.
def contacto(request):
    contacto1 = Persona(nombre = "Maria", apellido = "Lapida", email ="marialapida@yahoo.com.ar", tele = 1549332244)
    contacto1.save()
    
    contacto2 = Persona(nombre = "Roberto", apellido = "Gimenez", email ="robertgimenez@yahoo.com.ar", tele = 1540339449)
    contacto2.save()
    
    contacto3 = Persona(nombre = "Samuel", apellido = "Gimenez", email ="samgimenez@yahoo.com.ar", tele = 1540339449)
    contacto3.save()

    dict1 = { "nomb" : contacto1.nombre, "apell" : contacto1.apellido, "mail": contacto1.email, "tel": contacto1.tele }
    dict2 = { "nomb" : contacto2.nombre, "apell" : contacto2.apellido, "mail": contacto2.email, "tel": contacto2.tele }
    dict3 = { "nomb" : contacto3.nombre, "apell" : contacto3.apellido, "mail": contacto3.email, "tel": contacto3.tele }

    dict_padre = {"d1" : dict1, "d2" : dict2, "d3" : dict3, "dia" : datetime.datetime.now()}

    plantilla = loader.get_template("template1.html")

    return HttpResponse( plantilla.render(dict_padre))