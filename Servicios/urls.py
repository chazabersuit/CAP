
from django.urls import path

from Servicios.views import inicio, crear, listado

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear/', crear, name="crear"),
    path('listado/', listado, name="listado"),
]
