from django.urls import path
from . import views


urlpatterns = [
    path('tempos_tecnico/', views.TempoTecnicoCreateListView.as_view(), name= 'tempos_tecnico-create-list'),
    path('tempos_tecnico/<int:pk>/', views.TempoTecnicoRetrieveUpdateDestroyView.as_view(), name= 'tempos_tecnico-detail-view'),
]