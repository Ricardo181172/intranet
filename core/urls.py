from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('api/v1/', include('autenticacao.urls')),
    #path('api/v1/', include('ordens_servico.urls')),
    path('api/v1/', include('tecnicos.urls')),
    path('api/v1/', include('tempos_tecnico.urls')),
    
]
