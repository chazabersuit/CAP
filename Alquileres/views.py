from django.shortcuts import render

# Create your views here.

def crear_alquiler(request):
    mensaje= "hola alta"
    return render(request,'Alquileres/crear_alquiler.html',{'mensaje':mensaje})