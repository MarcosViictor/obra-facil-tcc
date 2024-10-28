from django import forms
from obras.models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome', 'descricao', 'quantidade', 'preco_unitario', 'data_compra', 'fornecedor', 'obra']
        widgets = {
            'data_compra': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}),  
        }

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade

    def clean_preco_unitario(self):
        preco_unitario = self.cleaned_data.get('preco_unitario')
        if preco_unitario <= 0:
            raise forms.ValidationError("O preço unitário deve ser maior que zero.")
        return preco_unitario