from django.shortcuts import render
# Crear una instruccion que le muestre o le salude al usuario
# para poder verla en web.
from django.http import HttpResponse

# Create your views here.

# Declarar funcion que nos permita imprimir un
# mensaje al usuario
def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi sistema</h1>")
