from django.urls import path
from .api import *
from .views import *
urlpatterns = [
    # Rutas apis basadas en funciones
    path('api/', EmpresaListCreateView.as_view(), name='empresa_list_create'),
    path('api/<uuid:id>/', EmpresaRetrieveUpdateDestroyView.as_view(), name='empresa_retrieve_update_destroy'),
    # Rutas para las vistas basadas en funciones
    path('listar/', listar_empresas, name='listar_empresas'),
    path('crear/', crear_empresa, name='crear_empresa'),
    path('editar/<uuid:id>/', editar_empresa, name='editar_empresa'),
    path('eliminar/<uuid:id>/', eliminar_empresa, name='eliminar_empresa'),
]
