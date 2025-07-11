from django.db import models

class Poste(models.Model):
    problema = models.CharField(max_length=200)
    informacao = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.problema} - ({self.latitude}, {self.longitude})"
