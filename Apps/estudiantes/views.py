from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import estudiantes # Asegúrate que el nombre del modelo sea correcto, por defecto es 'Estudiante' si tu modelo se llama así.
from .forms import EstudianteForm
from django.urls import reverse_lazy

class EstuView(ListView): # Renombramos la clase para mayor claridad y evitar conflictos
    model = estudiantes  # Especifica el modelo que quieres listar
    template_name = 'estudiantes.html'  # El nombre de tu template
    context_object_name = 'lista_estudiantes'  # El nombre de la variable que contendrá la lista en el template


class CrearEstudianteView(CreateView):
    template_name = 'crear.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiantes:estuapp')


class EditarEstudianteView(UpdateView):
    template_name = 'editar.html'
    model = estudiantes
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiantes:estuapp')


class VerDetailView(DetailView):
    model = estudiantes
    template_name = 'ver.html'
