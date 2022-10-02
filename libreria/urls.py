# Este archivo sirve para controlar las urls
# que querramos pero propias de la aplicacion
from django.urls import path

# Para poder acceder a las vistas
from . import views

# Aqui significa que el usuario va a poder entrar y va a
# poder acceder a lo que es las vistas (views.py)

# "inicio" es el nombre de la vista que declaramos en views.py
urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Crear acceso a Nosotros
    path('nosotros', views.nosotros, name='nosotros'),
    # Acceder a libros
    path('libros', views.libros, name='libros'),
]