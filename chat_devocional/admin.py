from django.contrib import admin
from .models import SessaoDevocional, MensagemDevocional

@admin.register(SessaoDevocional)
class SessaoDevocionalAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tema', 'data_inicio']
    list_filter = ['tema']

@admin.register(MensagemDevocional)
class MensagemDevocionalAdmin(admin.ModelAdmin):
    list_display = ['sessao', 'remetente', 'texto', 'data_hora']
