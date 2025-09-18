# Create your views here.

from django.views.generic import ListView, CreateView
from .models import Administradores
from .forms import AdminForm
from django.urls import reverse_lazy

class AdminView(ListView):
    model = Administradores
    template_name = 'admin.html'
    context_object_name = 'lista_administradores'

class CrearAdminView(CreateView):
    template_name = 'crearadmin.html'
    form_class = AdminForm
    success_url = reverse_lazy('administradores:adminapp')