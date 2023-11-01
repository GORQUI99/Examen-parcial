from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('listar/', listar_inventarios, name='listar_inventarios'),
    path('crear/', crear_inventario, name='crear_inventario'),
    path('editar/<uuid:id>/', editar_inventario, name='editar_inventario'),
    path('eliminar/<uuid:id>/', eliminar_inventario, name='eliminar_inventario'),

    # APIs
    path('crud/', InventariosListCreateView.as_view(), name='inventario_list_create'),
    path('crud/<uuid:id>/', InventariosRetrieveUpdateDestroyView.as_view(), name='inventario_retrieve_update_destroy'),
]
