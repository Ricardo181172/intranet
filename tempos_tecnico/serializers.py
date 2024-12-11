from rest_framework import serializers
from tempos_tecnico.models import TempoTecnico
from tecnicos.models import Tecnico
from tecnicos.serializers import TecnicoSerializer


class TempoTecnicoModelSerializer(serializers.ModelSerializer):

    EMP_CodEmpresa = serializers.CharField()
    EMP_CodFilial = serializers.CharField()
    USR_NomeUsuario = serializers.CharField()
    USR_CodUsuario = serializers.PrimaryKeyRelatedField(
        queryset=Tecnico.objects.all(),
    ) 
    USR_CodUsuario
    USR_idUsuario = serializers.IntegerField()
    USR_Ativo = serializers.IntegerField()
    USR_CodAreaOperacao = serializers.CharField()
    TMP_Ano = serializers.IntegerField()
    TMP_Mes = serializers.IntegerField()
    TMP_MinutosDisponivel = serializers.FloatField()
    dthRegistro = serializers.DateField()