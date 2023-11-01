from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # ... tus rutas existentes ...

    # Añadiendo las rutas para las vistas y API de ItemsInventario
    path('listar/', listar_items_inventario, name='listar_items_inventario'),
    path('crear/', crear_items_inventario, name='crear_items_inventario'),
    path('editar/<uuid:id>/', editar_items_inventario, name='editar_items_inventario'),
    path('eliminar/<uuid:id>/', eliminar_items_inventario, name='eliminar_items_inventario'),
    # ... tus otras rutas ...
    
    # APIs
    path('crud/', ItemInventarioListCreateView.as_view(), name='items_inventario_list_create'),
    path('crud/<uuid:id>/', ItemInventarioRetrieveUpdateView.as_view(), name='items_inventario_retrieve_update_destroy'),
]
