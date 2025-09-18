from django import forms 
from .models import Publicaciones

class PubliForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = '__all__'