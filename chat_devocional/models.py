from django.db import models
from django.contrib.auth.models import User

TEMA_CHOICES = [
    ('fe', 'Fé'),
    ('esperanca', 'Esperança'),
    ('gratidao', 'Gratidão'),
    ('perdao', 'Perdão'),
    ('oracao', 'Oração'),
    ('familia', 'Família'),
    ('proposito', 'Propósito'),
    ('superacao', 'Superação'),
]

class SessaoDevocional(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessoes_devocionais')
    tema = models.CharField(max_length=50, choices=TEMA_CHOICES, default='fe')
    data_inicio = models.DateTimeField(auto_now_add=True)
    resumo = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Sessão Devocional'
        verbose_name_plural = 'Sessões Devocionais'

    def __str__(self):
        return f'{self.usuario.username} - {self.get_tema_display()} - {self.data_inicio.date()}'


class MensagemDevocional(models.Model):
    sessao = models.ForeignKey(SessaoDevocional, on_delete=models.CASCADE, related_name='mensagens')
    remetente = models.CharField(max_length=10, choices=[('usuario', 'Usuário'), ('ia', 'IA')])
    texto = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_hora']
        verbose_name = 'Mensagem Devocional'
        verbose_name_plural = 'Mensagens Devocionais'

    def __str__(self):
        return f'{self.remetente}: {self.texto[:50]}'
