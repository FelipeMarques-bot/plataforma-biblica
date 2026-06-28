from django.contrib import admin
from .models import DesafioDiario, DesafioDiarioConcluido, Recompensa, RecompensaUsuario, SerieOuroDesafio, SerieOuroExercicio, SerieOuroProgresso, UserActivityLog

@admin.register(DesafioDiario)
class DesafioDiarioAdmin(admin.ModelAdmin):
    list_display = ['data', 'titulo', 'xp_recompensa', 'ativo']
    list_filter = ['ativo']

@admin.register(DesafioDiarioConcluido)
class DesafioDiarioConcluidoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'desafio', 'data_conclusao']

@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'xp_recompensa', 'ativo']
    list_filter = ['tipo', 'ativo']

@admin.register(RecompensaUsuario)
class RecompensaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'recompensa', 'aberto', 'data_desbloqueio']

@admin.register(SerieOuroDesafio)
class SerieOuroDesafioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'faixa_etaria', 'nivel', 'ativo']

@admin.register(SerieOuroExercicio)
class SerieOuroExercicioAdmin(admin.ModelAdmin):
    list_display = ['enunciado', 'desafio_ouro', 'tipo']

@admin.register(SerieOuroProgresso)
class SerieOuroProgressoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'desafio_ouro', 'concluido']

@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tipo_atividade', 'descricao_resumida', 'xp_ganho', 'data_hora']
    list_filter = ['tipo_atividade', 'data_hora']
    search_fields = ['usuario__username', 'usuario__email', 'descricao_resumida']
    date_hierarchy = 'data_hora'
