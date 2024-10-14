from django import forms
from obras.models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'funcao', 'obra']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Função'}),
            'obra': forms.Select(attrs={'class': 'form-select'}),
        }
