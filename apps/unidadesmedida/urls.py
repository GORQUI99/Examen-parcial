# En urls.py
from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # Añadiendo las rutas para las vistas de Unidades de Medida
    path('listar/', listar_unidades_medida, name='listar_unidades_medida'),
    path('crear/', crear_unidad_medida, name='crear_unidad_medida'),
    path('editar/<uuid:id>/', editar_unidad_medida, name='editar_unidad_medida'),
    path('eliminar/<uuid:id>/', eliminar_unidad_medida, name='eliminar_unidad_medida'),
    # APIs
    path('crud/', UnidadMedidaListCreateView.as_view(), name='unidad_medida_list_create'),
    path('crud/<uuid:id>/', UnidadMedidaRetrieveUpdateDestroyView.as_view(), name='unidad_medida_retrieve_update_destroy'),
]
