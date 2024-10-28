from django import forms
from obras.models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'funcao','obra', 'salario']  # Certifique-se de incluir 'salario'
