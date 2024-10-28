from django import forms
from obras.models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome', 'descricao', 'quantidade', 'preco_total', 'data_compra', 'fornecedor', 'obra']
        widgets = {
            'data_compra': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}),  # Formato padrão de data
        }

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade

    def clean_preco_total(self):
        preco_total = self.cleaned_data.get('preco_total')
        if preco_total <= 0:
            raise forms.ValidationError("O preço total deve ser maior que zero.")
        return preco_total
