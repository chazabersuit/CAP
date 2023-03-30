from django.db import models

# Create your models here.

#Base de dato
class Prueba(models.Model):
    nombre= models.CharField(max_length=30)
    edad= models.IntegerField()
    fecha_creacion=models.DateField(null=True)