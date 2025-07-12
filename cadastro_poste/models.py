from django.db import models

class Poste(models.Model):
    problema = models.CharField(max_length=200)
    informacao = models.TextField()

    cep = models.CharField(max_length=9, default='Desconhecido')
    rua = models.CharField(max_length=255, default='Desconhecido')
    numero = models.CharField(max_length=10, default='Desconhecido')
    bairro = models.CharField(max_length=100, default='Desconhecido')
    cidade = models.CharField(max_length=100, default='Desconhecido')
    estado = models.CharField(max_length=2, default='--')

    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.problema} - {self.rua}, {self.numero} - {self.bairro}"
