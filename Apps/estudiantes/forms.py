from django import forms
from .models import estudiantes

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = estudiantes
        fields = '__all__'