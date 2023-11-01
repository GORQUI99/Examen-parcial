from rest_framework import generics
from common.models import SublineasArticulos
from .serializers import SublineaSerializer

class SublineaListCreateView(generics.ListCreateAPIView):
    queryset = SublineasArticulos.objects.all()
    serializer_class = SublineaSerializer

class SublineaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SublineasArticulos.objects.all()
    serializer_class = SublineaSerializer
