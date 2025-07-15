from django import forms
from .models import Manutencao


class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = [
            'poste',
            'lampada',
            'data_manutencao',
            'tipo',
            'descricao',
            'status',
            'responsavel',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsavel'].disabled = True
