from django.db import models
from tecnicos.models import Tecnico

class TempoTecnico(models.Model):
    EMP_CodEmpresa = models.CharField(null=True, max_length=10)
    EMP_CodFilial = models.CharField(null=True, max_length=10)
    USR_NomeUsuario = models.CharField(null=True, max_length=200)
    USR_CodUsuario = models.ForeignKey(
        Tecnico,
        to_field='USR_CodUsuario', 
        on_delete=models.PROTECT,
        related_name='tecnicos'
    )
    USR_CodUsuario
    USR_idUsuario = models.IntegerField(primary_key=True)
    USR_Ativo = models.IntegerField()
    USR_CodAreaOperacao = models.CharField(null=True, max_length=10)
    TMP_Ano = models.IntegerField()
    TMP_Mes = models.IntegerField()
    TMP_MinutosDisponivel = models.FloatField(null=True)
    dthRegistro = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.USR_idUsuario
