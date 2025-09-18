from django.views.generic import ListView, CreateView
from .models import Publicaciones
from .forms import PubliForm
from django.urls import reverse_lazy

class PubliView(ListView):
    model = Publicaciones
    template_name='publicaciones.html'
    context_object_name = 'lista_publicaciones'

class CrearPubliView(CreateView):
    template_name = 'crearpubli.html'
    form_class = PubliForm
    success_url = reverse_lazy('publicaciones:publiapp')
