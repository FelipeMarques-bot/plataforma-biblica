from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_trilhas, name='lista_trilhas'),
    path('trilha/<int:trilha_id>/', views.mapa_trilha, name='mapa_trilha'),
    path('licao/<int:licao_id>/', views.licao_view, name='licao'),
    path('licao/<int:licao_id>/verificar/', views.verificar_resposta, name='verificar_resposta'),
    path('licao/<int:licao_id>/finalizar/', views.finalizar_licao, name='finalizar_licao'),
]
