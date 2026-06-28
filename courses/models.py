from django.db import models
from django.contrib.auth.models import User

TIPO_EXERCICIO_CHOICES = [
    ('MULTIPLA_ESCOLHA', 'Múltipla Escolha'),
    ('VF', 'Verdadeiro/Falso'),
    ('ASSOCIACAO', 'Associação'),
    ('ORDENACAO', 'Ordenação'),
]

class Trilha(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    faixa_etaria = models.CharField(max_length=20, choices=[
        ('crianca', 'Criança'), ('adolescente', 'Adolescente'), ('adulto', 'Adulto')
    ], default='adulto')
    nivel = models.CharField(max_length=20, choices=[
        ('iniciante', 'Iniciante'), ('intermediario', 'Intermediário'), ('avancado', 'Avançado')
    ], default='iniciante')
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    icone = models.CharField(max_length=10, default='📖')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'

    def __str__(self):
        return f'{self.nome} ({self.get_faixa_etaria_display()} - {self.get_nivel_display()})'


class LicaoBiblica(models.Model):
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE, related_name='licoes')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    texto_base = models.TextField(help_text='Texto ou referência bíblica')
    referencia = models.CharField(max_length=100, blank=True, help_text='Ex: Gênesis 1:1-31')
    objetivo = models.TextField(blank=True)
    resumo = models.TextField(blank=True)
    ordem = models.IntegerField(default=0)
    xp_recompensa = models.IntegerField(default=50)

    class Meta:
        ordering = ['trilha', 'ordem']
        verbose_name = 'Lição Bíblica'
        verbose_name_plural = 'Lições Bíblicas'

    def __str__(self):
        return f'{self.trilha.nome} - {self.titulo}'


class Exercicio(models.Model):
    licao = models.ForeignKey(LicaoBiblica, on_delete=models.CASCADE, related_name='exercicios')
    tipo = models.CharField(max_length=20, choices=TIPO_EXERCICIO_CHOICES, default='MULTIPLA_ESCOLHA')
    enunciado = models.TextField()
    dados = models.JSONField(help_text='JSON com alternativas, respostas etc.')
    peso_dificuldade = models.IntegerField(default=1)
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ['licao', 'ordem']

    def __str__(self):
        return f'{self.licao.titulo} - {self.enunciado[:50]}'


class ProgressoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progresso')
    licao = models.ForeignKey(LicaoBiblica, on_delete=models.CASCADE)
    concluida = models.BooleanField(default=False)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    xp_ganho_sessao = models.IntegerField(default=0)
    respostas = models.JSONField(default=dict, blank=True)

    class Meta:
        unique_together = ['usuario', 'licao']
        verbose_name = 'Progresso do Usuário'
        verbose_name_plural = 'Progressos dos Usuários'

    def __str__(self):
        return f'{self.usuario.username} - {self.licao.titulo}'
