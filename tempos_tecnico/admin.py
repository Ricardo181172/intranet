from django.contrib import admin
from tempos_tecnico.models import TempoTecnico


@admin.register(TempoTecnico)
class TempoTecnicoAdmin(admin.ModelAdmin):
    list_display = ('EMP_CodEmpresa', 
                    'EMP_CodFilial',
                    'USR_NomeUsuario', 
                    'USR_CodUsuario',
                    'USR_idUsuario',
                    'USR_Ativo',
                    'USR_CodAreaOperacao',
                    'TMP_Ano',
                    'TMP_Mes',
                    'TMP_MinutosDisponivel',
                    'dthRegistro'
                )