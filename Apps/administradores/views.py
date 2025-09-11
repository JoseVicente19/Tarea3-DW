# Create your views here.

from django.views.generic import ListView
from .models import Administradores

class AdminView(ListView):
    model = Administradores
    template_name = 'admin.html'
    context_object_name = 'lista_administradores'