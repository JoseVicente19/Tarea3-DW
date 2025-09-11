from django.views.generic import ListView
from .models import Publicaciones

class PubliView(ListView):
    model = Publicaciones
    template_name='publicaciones.html'
    context_object_name = 'lista_publicaciones'