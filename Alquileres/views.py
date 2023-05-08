from django.shortcuts import render
from .forms import Formulario_Alquiler
from .models import Alquileres

# Create your views here.

def crear_alquiler(request):
    formulario_alquiler=Formulario_Alquiler()
    lista= Alquileres.objects.all()
    
    
    if request.method== 'POST':
        formulario_alquiler=Formulario_Alquiler(request.POST)
        
        if formulario_alquiler.is_valid():
            data=formulario_alquiler.cleaned_data
            datos= Alquileres(
                nombre=data.get('nombre'),
                cuit=data.get('cuit'),
                direccion=data.get('direccion'),
                inicio_contrato=data.get('inicio_contrato'),
                sector=data.get('sector'),
                lugar=data.get('lugar'),)
            datos.save()
            datos=Alquileres.objects.all()
            return render(request, 'Alquileres/listado_alquiler.html',{'datos':datos})
        else:
            return render(request,'Alquileres/crear_alquiler.html',{'formulario_alquiler':formulario_alquiler})
    
    return render(request,'Alquileres/crear_alquiler.html',{'formulario_alquiler':formulario_alquiler,"lista":lista})

def listado_alquiler(request):
    lista= Alquileres.objects.all()
    return render(request,'Alquileres/listado_alquiler.html',{"lista":lista})