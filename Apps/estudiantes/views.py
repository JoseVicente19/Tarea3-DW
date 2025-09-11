from django.views.generic import ListView
from .models import estudiantes # Asegúrate que el nombre del modelo sea correcto, por defecto es 'Estudiante' si tu modelo se llama así.

class EstuView(ListView): # Renombramos la clase para mayor claridad y evitar conflictos
    model = estudiantes  # Especifica el modelo que quieres listar
    template_name = 'estudiantes.html'  # El nombre de tu template
    context_object_name = 'lista_estudiantes'  # El nombre de la variable que contendrá la lista en el template