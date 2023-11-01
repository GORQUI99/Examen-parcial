#urls.py
from django.urls import path
from .api import *
from .views import *

urlpatterns = [
    # ... tus rutas existentes ...
    path('crud/', SucursalListCreateView.as_view(), name='sucursal_list_create'),
    path('crud/<uuid:id>/', SucursalRetrieveUpdateDestroyView.as_view(), name='sucursal_retrieve_update_destroy'),
 # Añadiendo las rutas para las vistas basadas en funciones
    path('listar/', listar_sucursales, name='listar_sucursales'),
    path('crear/', crear_sucursal, name='crear_sucursal'),
    path('editar/<uuid:id>/', editar_sucursal, name='editar_sucursal'),
    path('eliminar/<uuid:id>/', eliminar_sucursal, name='eliminar_sucursal'),
]