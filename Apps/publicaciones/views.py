from django.views.generic import ListView, CreateView, UpdateView, DetailView
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

class EditarPubliView(UpdateView):
    template_name = 'editarpubli.html'
    model = Publicaciones
    form_class = PubliForm
    success_url = reverse_lazy('publicaciones:publiapp')

class PublicacionDetailView(DetailView):
    model = Publicaciones
    template_name = 'verpublicacion.html' 
