from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario


@receiver(post_save, sender=User)
def criar_ou_salvar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)
    else:
        perfil, created = PerfilUsuario.objects.get_or_create(user=instance)
        perfil.save()
