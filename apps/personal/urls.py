from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # ... tus rutas existentes ...
    
    # Añadiendo las rutas para las vistas de Personal
    path('listar/', listar_personal, name='listar_personal'),
    path('crear/', crear_personal, name='crear_personal'),
    path('editar/<uuid:id>/', editar_personal, name='editar_personal'),
    path('eliminar_personal/<uuid:id>/', eliminar_personal, name='eliminar_personal'),

    # APIs
    path('crud/', PersonalListCreateView.as_view(), name='personal_list_create'),
    path('crud/<uuid:id>/', PersonalRetrieveUpdateDestroyView.as_view(), name='personal_retrieve_update_destroy'),
]
