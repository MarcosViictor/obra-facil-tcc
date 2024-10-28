from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from obras.models import ConsumoMaterial, Material
from obras.forms.materialConsumo import ConsumoMaterialForm

class ConsumoMaterialCreateView(CreateView):
    model = ConsumoMaterial
    form_class = ConsumoMaterialForm
    template_name = 'materiais/consumo_material_form.html'
    success_url = reverse_lazy('obra-list')

    def form_valid(self, form):
        # Carrega o material atualizado diretamente do banco para garantir que o valor esteja correto
        material = get_object_or_404(Material, pk=form.cleaned_data['material'].pk)
        quantidade_consumida = form.cleaned_data['quantidade_consumida']

        # Atualiza a quantidade do material
        if material.quantidade >= quantidade_consumida:
            material.quantidade -= quantidade_consumida
            material.save()
        else:
            messages.error(self.request, 'Erro: a quantidade consumida é maior que a disponível.')
            return self.form_invalid(form)  # Retorna para o formulário com o erro

        # Exibe uma mensagem de sucesso
        messages.success(self.request, 'Consumo de material registrado com sucesso!')
        return super().form_valid(form)