from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class InfoView(TemplateView):
    template_name='informacion.html'
