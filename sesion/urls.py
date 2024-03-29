from django.urls import path

from django.contrib.auth import views as auth_views
from sesion import views


app_name='sesion'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('misdatos/', views.misdatos,name='misdatos'),
]
