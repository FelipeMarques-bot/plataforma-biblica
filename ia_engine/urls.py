from django.urls import path
from . import views

urlpatterns = [
    path('dica/<int:exercicio_id>/', views.pedir_dica, name='pedir_dica'),
    path('explicar/<int:licao_id>/', views.explicar_licao, name='explicar_licao'),
    path('devocional/', views.devocional_view, name='devocional_ia'),
]
