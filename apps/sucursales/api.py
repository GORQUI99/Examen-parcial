from rest_framework import generics
from common.models import Sucursales
from .serializers import SucursalSerializer
class SucursalListCreateView(generics.ListCreateAPIView):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalSerializer

class SucursalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalSerializer
