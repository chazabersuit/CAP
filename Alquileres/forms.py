from django import forms

class Formulario_Alquiler(forms.Form):
    nombre=forms.CharField(max_length=30)
    cuit=forms.IntegerField()
    direccion=forms.CharField(max_length=30)
    inicio_contrato=forms.DateField()
    sector=forms.IntegerField()
    lugar=forms.IntegerField()