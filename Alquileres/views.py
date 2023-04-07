from django.shortcuts import render
from .forms import Formulario_Alquiler

# Create your views here.

def crear_alquiler(request):
    formulario_alquiler=Formulario_Alquiler()
    
    return render(request,'Alquileres/crear_alquiler.html',{'formulario_alquiler':formulario_alquiler})