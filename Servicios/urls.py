
from django.urls import path

from Servicios.views import inicio, crear_servicios, listado_servicios

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear_servicios/', crear_servicios, name="crear_servicios"),
    path('listado_servicios/', listado_servicios, name="listado_servicios"),
]
