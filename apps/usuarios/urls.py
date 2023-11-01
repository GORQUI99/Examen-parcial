# En urls.py
from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('register/', crear_usuario, name='register'),
]