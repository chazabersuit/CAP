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
   miformulario=Formulario()
   if request.method== 'POST':
      form=Formulario(request.POST)
      if form.is_valid():
         data= form.cleaned_data
         datos=Formulario(nombre=data.get('nombre'),edad=data.get('edad'),fecha_creacion=datetime.now())  
         datos.save()
         return render(request,'exito.html', {})
      else:
         return render(request,'crear.html',{'miformulario':form})
      
   
   return render(request,'crear.html',{'miformulario':miformulario})