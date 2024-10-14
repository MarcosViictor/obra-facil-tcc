from django import forms
from obras.models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome', 'descricao', 'quantidade', 'preco_unitario', 'data_compra', 'obra', 'fornecedor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Material'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
            'preco_unitario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço Unitário'}),
            'data_compra': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data da Compra', 'type': 'date'}),
            'obra': forms.Select(attrs={'class': 'form-select'}),
            'fornecedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fornecedor'}),
        }
