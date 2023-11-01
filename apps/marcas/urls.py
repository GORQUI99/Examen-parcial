# En urls.py
from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # ... tus rutas existentes ...
    
    # Añadiendo las rutas para las vistas de Marcas
    path('listar/', listar_marcas, name='listar_marcas'),
    path('crear/', crear_marca, name='crear_marcas'),
    path('editar/<uuid:id>/', editar_marca, name='editar_marcas'),
    path('eliminar/<uuid:id>/', eliminar_marca, name='eliminar_marcas'),
    #apis
    path('crud/', MarcaListCreateView.as_view(), name='marca_list_create'),
    path('crud/<uuid:id>/', MarcaRetrieveUpdateDestroyView.as_view(), name='marca_retrieve_update_destroy'),
]