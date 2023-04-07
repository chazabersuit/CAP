
from django.urls import path
from .views import crear_alquiler

urlpatterns = [
    path('crear_alquiler/', crear_alquiler, name="crear_alquiler"),
]