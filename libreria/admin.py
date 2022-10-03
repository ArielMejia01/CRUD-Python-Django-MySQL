from django.contrib import admin
# la informacion que voy a utilizar esta en modelo
from .models import Libro

# Register your models here.
# Registrar toda la informacion que necesito
# Una vez incluido el Libro ya lo tenemos a disposicion en nuestro modelo
# y tenemos que registrarlo en el administrador
# ya cuando corramos el administrador ya tenga la manipulacion de ese libro
admin.site.register(Libro)