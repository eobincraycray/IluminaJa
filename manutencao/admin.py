from django.contrib import admin
from .models import Manutencao


@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'poste', 'lampada', 'data_manutencao',
                    'tipo', 'status', 'responsavel')
    list_filter = ('tipo', 'status', 'data_manutencao')
    search_fields = ('poste__id', 'lampada__id',
                     'descricao', 'responsavel__username')
