from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from obras.models import Obra
from django.urls import reverse_lazy

class ObraListView(ListView):
    model = Obra
    template_name = 'obra/obra_list.html'

class ObraDetailView(DetailView):
    model = Obra
    template_name = 'obra/obra_detail.html'

class ObraCreateView(CreateView):
    model = Obra
    fields = ['nome', 'descricao', 'endereco', 'data_inicio', 'dt_prev_fim', 'gerente', 'mestres']
    template_name = 'obra/obra_form.html'
    
    def get_success_url(self):
        return reverse('obra-list')  # O 'obra-list' é o nome da URL

class ObraUpdateView(UpdateView):
    model = Obra
    fields = ['nome', 'descricao', 'endereco', 'data_inicio', 'dt_prev_fim', 'gerente', 'mestres']
    template_name = 'obra/obra_form.html'

class ObraDeleteView(DeleteView):
    model = Obra
    template_name = 'obra/obra_confirm_delete.html'
    success_url = reverse_lazy('obra-list')