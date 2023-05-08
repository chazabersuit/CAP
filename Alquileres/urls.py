
from django.urls import path
from .views import crear_alquiler, listado_alquiler

urlpatterns = [
    path('crear_alquiler/', crear_alquiler, name="crear_alquiler"),
    path('listado_alquiler/', listado_alquiler, name="listado_alquiler"),
]