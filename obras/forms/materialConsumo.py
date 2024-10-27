from django import forms
from obras.models import ConsumoMaterial

class ConsumoMaterialForm(forms.ModelForm):
    class Meta:
        model = ConsumoMaterial
        fields = ['material', 'quantidade_consumida', 'obra']

    def clean_quantidade_consumida(self):
        quantidade_consumida = self.cleaned_data.get('quantidade_consumida')
        material = self.cleaned_data.get('material')

        # Verifica se a quantidade consumida excede a quantidade disponível
        if quantidade_consumida and material and quantidade_consumida > material.quantidade:
            raise forms.ValidationError("A quantidade consumida excede a quantidade disponível.")
        return quantidade_consumida
