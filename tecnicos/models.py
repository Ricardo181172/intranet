from django.db import models

class Tecnico(models.Model):
    USR_idUsuario = models.IntegerField()
    USR_CPF = models.CharField(null=True, max_length=14)
    USR_nomeUsuario = models.CharField(null=True, max_length=200)
    USR_Login = models.CharField(null=True, max_length=200)
    USR_TipoUsuario = models.CharField(null=True, max_length=1) 
    USR_dscTipoUsuario = models.CharField(null=True, max_length=16)
    USR_idEmpresa = models.IntegerField()
    USR_Email = models.CharField(null=True, max_length=255)
    USR_idLicenca = models.CharField(null=True, max_length=255)
    USR_dthRegistro = models.DateTimeField(null=True, blank=True)
    USR_CodUsuario = models.CharField(max_length=20, primary_key=True)
    EMP_idEmpresa = models.IntegerField()
    EMP_nome = models.CharField(null=True, max_length=200)
    EMP_cidade = models.CharField(null=True, max_length=100)
    EMP_CodFilial = models.CharField(null=True, max_length=10)
    dthRegistro = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.USR_CodUsuario