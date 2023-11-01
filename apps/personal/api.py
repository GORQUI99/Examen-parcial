from rest_framework import generics
from common.models import Personal
from .serializers import PersonalSerializer

class PersonalListCreateView(generics.ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class PersonalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
