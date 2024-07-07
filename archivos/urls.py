from django.urls import path
from . import views

urlpatterns = [
    path('subirArchivo', views.subirArchivo, name="subirArchivo"),
    path('subirArchivoBinario', views.subirArchivoTemplate, name="subirArchivoTemplate"),
    path('catalogoArchivos', views.catalogoArchivos, name="catalogoArchivos"),
    path('correo', views.correo)
]