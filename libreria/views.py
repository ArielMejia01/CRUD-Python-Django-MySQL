from django.shortcuts import render
# Crear una instruccion que le muestre o le salude al usuario
# para poder verla en web.
from django.http import HttpResponse

# Create your views here.

# Declarar funcion que nos permita imprimir un
# mensaje al usuario
def inicio(request):
    return render(request, 'paginas/inicio.html')

# Nosotros necesitamos acceder al archivo html asi que hacemos
# uso de render.
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# Acceder a libros
def libros(request):
    return render(request, 'libros/index.html')