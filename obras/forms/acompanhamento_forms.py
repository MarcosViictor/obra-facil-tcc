from django import forms
from obras.models import Acompanhamento

class AcompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Acompanhamento
        fields = ['obra', 'descricao', 'progresso', 'mestre_responsavel']
