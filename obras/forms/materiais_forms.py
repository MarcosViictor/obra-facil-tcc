from django import forms
from obras.models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome', 'descricao', 'quantidade', 'quantidade_consumida', 'preco_unitario', 'data_compra', 'fornecedor', 'obra']
        widgets = {
            'data_compra': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_quantidade_consumida(self):
        """Verifica se a quantidade consumida não é maior que a quantidade disponível."""
        quantidade = self.cleaned_data.get('quantidade')
        quantidade_consumida = self.cleaned_data.get('quantidade_consumida')

        if quantidade_consumida > quantidade:
            raise forms.ValidationError("A quantidade consumida não pode ser maior que a quantidade total.")

        return quantidade_consumida
