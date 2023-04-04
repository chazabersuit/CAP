from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Formulario
from .models import Prueba

# Create your views here.
def inicio (request):
   
   return render(request, 'index.html',{})

def crear(request):
   # nombre= request.POST.get('nombre')
   # edad= request.POST.get('edad')
   # datos = Prueba(nombre=nombre,edad=edad, fecha_creacion=datetime.now())
   # datos.save()
   miformulario1=Formulario()
   
   if request.method== 'POST':
      miformulario=Formulario(request.POST)
      
      if miformulario.is_valid():
         data= miformulario.cleaned_data
         datos= Prueba(nombre=data.get('nombre'),edad=data.get('edad'), fecha_creacion=datetime.now())
         datos.save()
         mensaje='Guardado con exito'
         datos= Prueba.objects.all()
         return render(request,'listado.html', {'mensaje':mensaje,'datos':datos})
      else:
         return render(request,'crear.html',{'miformulario':miformulario})
      
   
   return render(request,'crear.html',{'miformulario':miformulario1})

def listado(request):
   datos= Prueba.objects.all()
   return render(request,'listado.html',{'datos':datos})