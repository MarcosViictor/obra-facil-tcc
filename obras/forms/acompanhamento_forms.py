
from django import forms
from obras.models import Acompanhamento

class AcompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Acompanhamento
        fields = ['obra', 'descricao', 'progresso', 'mestre_responsavel']
        widgets = {
            'obra': forms.Select(attrs={'class': 'form-control'}),  # Se preferir, pode remover as classes
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'progresso': forms.NumberInput(attrs={'class': 'form-control'}),
            'mestre_responsavel': forms.Select(attrs={'class': 'form-control'}),
        }
