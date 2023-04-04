from django.db import models

# Create your models here.

#Base de dato
class Prueba(models.Model):
    nombre= models.CharField(max_length=30, help_text="ingrese nombre")
    edad= models.IntegerField()
    fecha_creacion=models.DateField(null=True)
    
    def __str__(self):
        return self.nombre 