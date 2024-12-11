from django.urls import path
from . import views


urlpatterns = [
    path('tecnicos/', views.TecnicoCreateListView.as_view(), name= 'tecnico-create-list'),
    path('tecnicos/<str:pk>/', views.TecnicoRetrieveUpdateDestroyView.as_view(), name= 'tecnico-detail-view'),
]