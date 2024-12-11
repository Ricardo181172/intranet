from rest_framework import serializers
from tecnicos.models import Tecnico


class TecnicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tecnico
        fields = '__all__'