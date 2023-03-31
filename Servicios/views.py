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
 
         return render(request,'exito.html', {'data':data})
      else:
         return render(request,'crear.html',{'miformulario':miformulario})
      
   
   return render(request,'crear.html',{'miformulario':miformulario1})