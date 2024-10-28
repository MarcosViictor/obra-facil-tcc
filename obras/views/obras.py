from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from obras.models import Obra
from obras.forms.obras_forms import ObraForm

class ObraListView(ListView):
    model = Obra
    template_name = 'obra/obra_list.html'

class ObraDetailView(DetailView):
    model = Obra
    template_name = 'obra/obra_detail.html'

class ObraCreateView(CreateView):
    model = Obra
    form_class = ObraForm  # Usando o form criado
    template_name = 'obra/obra_form.html'
    
    def get_success_url(self):
        return reverse_lazy('obra-list')  # URL após criar a obra

class ObraUpdateView(UpdateView):
    model = Obra
    form_class = ObraForm  # Usando o form para update
    template_name = 'obra/obra_form.html'

    def get_success_url(self):
        return reverse_lazy('obra-detail', kwargs={'pk': self.object.pk})  # Redirecionando para o detalhe da obra

class ObraDeleteView(DeleteView):
    model = Obra
    template_name = 'obra/obra_confirm_delete.html'
    success_url = reverse_lazy('obra-list')
