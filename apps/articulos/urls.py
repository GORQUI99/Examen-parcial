#urls.py
from django.urls import path
from .api import *
from .views import *

urlpatterns = [
    # ... tus rutas existentes ...
    
    # Añadiendo las rutas para las vistas basadas en funciones
    path('listar/', listar_articulos, name='listar_articulos'),
    path('crear/', crear_articulo, name='crear_articulo'),
    path('editar/<uuid:id>/', editar_articulo, name='editar_articulo'),
    path('eliminar/<uuid:id>/', eliminar_articulo, name='eliminar_articulo'),

    # Añadiendo las rutas para las vistas basadas en clases (API)
    path('crud/', ArticuloListCreateView.as_view(), name='articulo_list_create'),
    path('crud/<uuid:id>/', ArticuloRetrieveUpdateDestroyView.as_view(), name='articulo_retrieve_update_destroy'),
]
