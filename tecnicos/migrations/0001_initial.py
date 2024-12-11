# Generated by Django 5.1.4 on 2024-12-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('USR_idUsuario', models.IntegerField()),
                ('USR_CPF', models.CharField(max_length=14, null=True)),
                ('USR_nomeUsuario', models.CharField(max_length=200, null=True)),
                ('USR_Login', models.CharField(max_length=200, null=True)),
                ('USR_TipoUsuario', models.CharField(max_length=1, null=True)),
                ('USR_dscTipoUsuario', models.CharField(max_length=16, null=True)),
                ('USR_idEmpresa', models.IntegerField()),
                ('USR_Email', models.CharField(max_length=255, null=True)),
                ('USR_idLicenca', models.CharField(max_length=255, null=True)),
                ('USR_dthRegistro', models.DateTimeField(blank=True, null=True)),
                ('USR_CodUsuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('EMP_idEmpresa', models.IntegerField()),
                ('EMP_nome', models.CharField(max_length=200, null=True)),
                ('EMP_cidade', models.CharField(max_length=100, null=True)),
                ('EMP_CodFilial', models.CharField(max_length=10, null=True)),
                ('dthRegistro', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
