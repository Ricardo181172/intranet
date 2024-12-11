from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from tecnicos.models import Tecnico
from tecnicos.serializers import TecnicoSerializer


class TecnicoCreateListView(generics.ListCreateAPIView):    
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class TecnicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = Tecnico.objects.all()   
    serializer_class = TecnicoSerializer
