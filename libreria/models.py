from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
# Captura toda la estructura de nuestra tabla
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    # Aqui se guardara la imagen que vamos a utilizar
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen" ,null=True)
    description = models.TextField(verbose_name="Descripcion", null=True)