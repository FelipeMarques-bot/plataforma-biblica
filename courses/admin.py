from django.contrib import admin
from .models import Trilha, LicaoBiblica, Exercicio, ProgressoUsuario

@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'faixa_etaria', 'nivel', 'ordem', 'ativo']
    list_filter = ['faixa_etaria', 'nivel', 'ativo']

@admin.register(LicaoBiblica)
class LicaoBiblicaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'trilha', 'ordem', 'xp_recompensa']
    list_filter = ['trilha']

@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ['enunciado', 'licao', 'tipo', 'ordem']

@admin.register(ProgressoUsuario)
class ProgressoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'licao', 'concluida', 'data_conclusao', 'xp_ganho_sessao']
    list_filter = ['concluida']
