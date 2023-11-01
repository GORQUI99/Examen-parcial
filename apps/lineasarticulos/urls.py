# En urls.py
from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # ... tus rutas existentes ...
    
    # Añadiendo las rutas para las vistas de Líneas de Artículos
    path('listar/', listar_lineas_articulos, name='listar_lineas_articulos'),
    path('crear/', crear_linea_articulos, name='crear_linea_articulos'),
    path('editar/<uuid:id>/', editar_linea_articulos, name='editar_linea_articulos'),
    path('eliminar_linea_articulos/<uuid:id>/', eliminar_linea_articulos, name='eliminar_linea_articulos'),

    # APIs
    path('crud/', LineasArticulosListCreateView.as_view(), name='linea_articulo_list_create'),
    path('crud/<uuid:id>/', LineasArticulosRetrieveUpdateDestroyView.as_view(), name='linea_articulo_retrieve_update_destroy'),
]
