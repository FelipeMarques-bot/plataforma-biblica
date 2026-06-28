from django.db import models
from django.contrib.auth.models import User
from courses.models import LicaoBiblica, Trilha

class DesafioDiario(models.Model):
    data = models.DateField(unique=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    versiculo = models.CharField(max_length=200, blank=True)
    pergunta = models.TextField(blank=True)
    xp_recompensa = models.IntegerField(default=30)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Desafio Diário'
        verbose_name_plural = 'Desafios Diários'

    def __str__(self):
        return f'{self.data} - {self.titulo}'


class DesafioDiarioConcluido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    desafio = models.ForeignKey(DesafioDiario, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=True)
    data_conclusao = models.DateTimeField(auto_now_add=True)
    xp_ganho = models.IntegerField(default=0)

    class Meta:
        unique_together = ['usuario', 'desafio']

    def __str__(self):
        return f'{self.usuario.username} - {self.desafio.titulo}'


class Recompensa(models.Model):
    TIPO_CHOICES = [
        ('versiculo', 'Versículo'),
        ('medalha', 'Medalha'),
        ('curiosidade', 'Curiosidade'),
        ('xp_bonus', 'Bônus de XP'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='medalha')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, default='🏅')
    xp_recompensa = models.IntegerField(default=100)
    criterio_licoes = models.IntegerField(default=0, help_text='Mínimo de lições concluídas')
    criterio_xp = models.IntegerField(default=0, help_text='XP mínimo')
    criterio_streak = models.IntegerField(default=0, help_text='Streak mínimo')
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Recompensa'
        verbose_name_plural = 'Recompensas'

    def __str__(self):
        return f'{self.titulo} ({self.get_tipo_display()})'


class RecompensaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recompensas')
    recompensa = models.ForeignKey(Recompensa, on_delete=models.CASCADE)
    aberto = models.BooleanField(default=False)
    data_desbloqueio = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['usuario', 'recompensa']

    def __str__(self):
        return f'{self.usuario.username} - {self.recompensa.titulo}'


class SerieOuroDesafio(models.Model):
    licao = models.ForeignKey(LicaoBiblica, on_delete=models.SET_NULL, null=True, blank=True)
    trilha = models.ForeignKey(Trilha, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    faixa_etaria = models.CharField(max_length=20, default='adulto')
    nivel = models.CharField(max_length=20, default='avancado')
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    xp_recompensa = models.IntegerField(default=150)

    class Meta:
        verbose_name = 'Série Ouro - Desafio'
        verbose_name_plural = 'Série Ouro - Desafios'

    def __str__(self):
        return self.titulo


class SerieOuroExercicio(models.Model):
    desafio_ouro = models.ForeignKey(SerieOuroDesafio, on_delete=models.CASCADE, related_name='exercicios')
    tipo = models.CharField(max_length=20, choices=[
        ('MULTIPLA_ESCOLHA', 'Múltipla Escolha'),
        ('VF', 'Verdadeiro/Falso'),
        ('ASSOCIACAO', 'Associação'),
        ('ORDENACAO', 'Ordenação'),
    ], default='MULTIPLA_ESCOLHA')
    enunciado = models.TextField()
    dados = models.JSONField()
    peso_dificuldade = models.IntegerField(default=2)

    def __str__(self):
        return f'{self.desafio_ouro.titulo} - {self.enunciado[:50]}'


class SerieOuroProgresso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    desafio_ouro = models.ForeignKey(SerieOuroDesafio, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    xp_ganho = models.IntegerField(default=0)
    pontos_para_ajuda_ganhos = models.IntegerField(default=0)

    class Meta:
        unique_together = ['usuario', 'desafio_ouro']

    def __str__(self):
        return f'{self.usuario.username} - {self.desafio_ouro.titulo}'
