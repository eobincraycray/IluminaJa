from django.db import models
from django.conf import settings
from cadastro_poste.models import Poste, Lampada


class Manutencao(models.Model):
    TIPO_MANUTENCAO_CHOICES = [
        ('substituicao', 'Substituição'),
        ('reparo', 'Reparo'),
        ('inspecao', 'Inspeção'),
        ('outro', 'Outro'),
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    poste = models.ForeignKey(
        Poste, on_delete=models.CASCADE, related_name='manutencoes')
    lampada = models.ForeignKey(
        Lampada, on_delete=models.CASCADE, related_name='manutencoes', null=True, blank=True)
    data_manutencao = models.DateField()
    tipo = models.CharField(max_length=20, choices=TIPO_MANUTENCAO_CHOICES)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pendente')
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Manutencao {self.id} - {self.get_tipo_display()} no Poste {self.poste.id}'
