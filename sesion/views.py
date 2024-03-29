from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url='misdatos'

    def get_success_url(self):
        return redirect('misdatos.hml')  # Ruta a la página de destino después del inicio de sesión

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context
    
@login_required
def misdatos(request):
    sesion=request
    
    return render(request,'registration/misdatos.html',{'sesion':sesion})