from django.contrib import admin
from tecnicos.models import Tecnico


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('USR_idUsuario', 
                    'USR_CPF', 
                    'USR_nomeUsuario', 
                    'USR_Login',
                    'USR_TipoUsuario',
                    'USR_dscTipoUsuario',
                    'USR_idEmpresa', 
                    'USR_Email', 
                    'USR_idLicenca', 
                    'USR_dthRegistro',
                    'USR_CodUsuario',
                    'EMP_idEmpresa',
                    'EMP_nome',
                    'EMP_cidade',
                    'EMP_CodFilial',
                    'dthRegistro'
                )
