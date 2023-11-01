from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # ... tus rutas existentes ...

    # Añadiendo las rutas para las vistas y API de GruposProveedor
    path('listar/', listar_grupos_proveedor, name='listar_grupos_proveedor'),
    path('crear/', crear_grupo_proveedor, name='crear_grupo_proveedor'),
    path('editar/<uuid:id>/', editar_grupo_proveedor, name='editar_grupo_proveedor'),
    path('eliminar/<uuid:id>/', eliminar_grupo_proveedor, name='eliminar_grupo_proveedor'),

    # APIs
    path('crud/', GruposProveedorListCreateView.as_view(), name='grupo_list_create'),
    path('crud/<uuid:id>/', GruposProveedorRetrieveUpdateDestroyView.as_view(), name='grupo_retrieve_update_destroy'),
]
