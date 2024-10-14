from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from obras.models import Material

class MaterialListView(ListView):
    model = Material
    template_name = 'materiais/material_list.html'
    context_object_name = 'materiais'

class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materiais/material_detail.html'
    context_object_name = 'material'

class MaterialCreateView(CreateView):
    model = Material
    fields = ['nome', 'descricao', 'quantidade', 'preco_unitario', 'data_compra', 'obra', 'fornecedor']
    template_name = 'materiais/material_form.html'

    def get_success_url(self):
        return reverse_lazy('material-list')

class MaterialUpdateView(UpdateView):
    model = Material
    fields = ['nome', 'descricao', 'quantidade', 'preco_unitario', 'data_compra', 'obra', 'fornecedor']
    template_name = 'materiais/material_form.html'

    def get_success_url(self):
        return reverse_lazy('material-list')

class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'materiais/material_confirm_delete.html'
    success_url = reverse_lazy('material-list')
