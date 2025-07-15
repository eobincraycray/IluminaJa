from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth import get_user_model
from .models import PerfilUsuario

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('id', 'username', 'email', 'first_name',
                    'is_active', 'is_staff', 'get_tipo_tecnico')
    search_fields = ('username', 'email', 'first_name')
    list_filter = ('is_active', 'is_staff')

    def get_tipo_tecnico(self, obj):
        try:
            return obj.perfilusuario.get_tipo_tecnico_display()
        except PerfilUsuario.DoesNotExist:
            return '-'
    get_tipo_tecnico.short_description = 'Tipo'
