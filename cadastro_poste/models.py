from django.db import models

class Poste(models.Model):

    STATUS_CHOICES = [
        (0, 'Recém adicionado'),
        (1, 'Aguardando'),
        (2, 'Cancelado'),
        (3, 'Corrigido'),
    ]
    problema = models.CharField(max_length=200)
    informacao = models.TextField()

    cep = models.CharField(max_length=9, default='Desconhecido')
    rua = models.CharField(max_length=255, default='Desconhecido')
    numero = models.CharField(max_length=10, default='Desconhecido')
    bairro = models.CharField(max_length=100, default='Desconhecido')
    cidade = models.CharField(max_length=100, default='Desconhecido')
    estado = models.CharField(max_length=2, default='--')

    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}"
    
    def get_status_display_label(self):
        return dict(self.STATUS_CHOICES).get(self.status, "Desconhecido")


class Lampada(models.Model):
    TIPO_CHOICES = [
        ('LED', 'LED'),
        ('Vapor de Sódio', 'Vapor de Sódio'),
        ('Fluorescente', 'Fluorescente'),
        ('Incandescente', 'Incandescente'),
        ('Halógena', 'Halógena'),
        ('Outros', 'Outros'),
    ]

    STATUS_CHOICES = [
        ('Funcionando', 'Funcionando'),
        ('Queimada', 'Queimada'),
        ('Substituída', 'Substituída'),
    ]

    poste = models.OneToOneField(Poste, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    potencia = models.PositiveIntegerField(default=60, help_text="Potência em Watts")
    vida_util_meses = models.PositiveIntegerField()
    data_instalacao = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.tipo} - {self.potencia}W no poste {self.poste.id}"
