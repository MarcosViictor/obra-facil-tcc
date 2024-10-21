from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from obras.models import ConsumoMaterial, Material
from obras.forms.materialConsumo import ConsumoMaterialForm

class ConsumoMaterialCreateView(CreateView):
    model = ConsumoMaterial
    form_class = ConsumoMaterialForm
    template_name = 'materiais/consumo_material_form.html'  # Defina o template que será renderizado
    success_url = reverse_lazy('obra-list')  # Redireciona para a lista de obras ou outro caminho

    def form_valid(self, form):
        material = form.cleaned_data['material']
        quantidade_consumida = form.cleaned_data['quantidade_consumida']

        # Subtrai a quantidade consumida da quantidade disponível do material
        material.quantidade -= quantidade_consumida
        material.save()

        # Exibe uma mensagem de sucesso
        messages.success(self.request, 'Consumo de material registrado com sucesso!')
        return super().form_valid(form)
