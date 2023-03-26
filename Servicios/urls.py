
from django.urls import path

from Servicios.views import inicio

urlpatterns = [
    path('', inicio),
]
