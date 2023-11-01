from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # ... tus rutas existentes ...

    # Añadiendo las rutas para las vistas de Sublíneas de Artículos
    path('listar/', listar_sublineas, name='listar_sublineas'),
    path('crear/', crear_sublinea, name='crear_sublinea'),
    path('editar/<uuid:id>/', editar_sublinea, name='editar_sublinea'),
    path('eliminar/<uuid:id>/', eliminar_sublinea, name='eliminar_sublinea'),

    # APIs
    path('crud/', SublineaListCreateView.as_view(), name='sublinea_list_create'),
    path('crud/<uuid:id>/', SublineaRetrieveUpdateDestroyView.as_view(), name='sublinea_retrieve_update_destroy'),
]
