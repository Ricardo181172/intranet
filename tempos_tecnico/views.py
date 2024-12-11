from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from tempos_tecnico.models import TempoTecnico
from tempos_tecnico.serializers import TempoTecnicoModelSerializer


class TempoTecnicoCreateListView(generics.ListCreateAPIView):    
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = TempoTecnico.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TempoTecnicoModelSerializer        
        return TempoTecnicoModelSerializer

class TempoTecnicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = TempoTecnico.objects.all()   
    serializer_class = TempoTecnicoModelSerializer
