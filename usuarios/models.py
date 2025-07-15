from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class PerfilUsuario(models.Model):
    TIPO_TECNICO_CHOICES = [
        ('tecnico', 'Técnico'),
        ('prefeitura', 'Representante da Prefeitura'),
        ('outro', 'Outro'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo_tecnico = models.CharField(
        max_length=50, choices=TIPO_TECNICO_CHOICES, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_tecnico_display()}"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
