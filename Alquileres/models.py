from django.db import models

# Create your models here.
class Alquileres(models.Model):
    nombre=models.CharField(max_length=30)
    cuit=models.IntegerField()
    direccion=models.CharField(max_length=30)
    inicio_contrato=models.DateField()
    
    def __str__(self):
        return self.nombre 