from django import forms

class Formulario(forms.Form):
    #aca se especifican los campos del formulario
    nombre = forms.CharField()
    edad= forms.IntegerField()
    fecha_creacion=forms.DateField()
    