from django import forms
from obras.models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['nome', 'descricao', 'endereco', 'data_inicio', 'dt_prev_fim', 'valor_total', 'progresso_total', 'gerente', 'mestres']
    
    def __init__(self, *args, **kwargs):
        super(ObraForm, self).__init__(*args, **kwargs)
        # Adicionando classes aos widgets
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})