"""
URL configuration for ColegioA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps.publicaciones import views
from .views import PubliView, CrearPubliView, EditarPubliView, PublicacionDetailView

app_name='publicaciones'
urlpatterns = [
    path('', PubliView.as_view(), name='publiapp'),
    path('/crear', CrearPubliView.as_view(), name='crearpubli'),
    path('/editar <int:pk>', EditarPubliView.as_view(), name='editarpubli'),
    path('/ver <int:pk>', PublicacionDetailView.as_view(), name='verpubli'),

]
