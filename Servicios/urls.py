
from django.urls import path

from Servicios.views import inicio, crear

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear/', crear, name="crear"),
]
