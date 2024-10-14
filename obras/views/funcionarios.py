from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from obras.models import Profissional

class ProfissionalListView(ListView):
    model = Profissional
    template_name = 'profissional/profissional_list'
    context_object_name = 'profissionais'

class ProfissionalDetailView(DetailView):
    model = Profissional
    template_name = 'profissional/profissional_detail'
    context_object_name = 'profissionais'
class ProfissionalCreateView(CreateView):
    model = Profissional
    fields = ['nome', 'funcao','obra']
    template_name= 'profissional/profissional_form'
    success_url = reverse_lazy('profissional-list')

class ProfissionalUpdateView(UpdateView):
    model = Profissional
    fields = ['nome', 'funcao', 'obra']
    template_name = 'profissional/profissional_form'
    success_url = reverse_lazy('profissional-list')

class ProfissionalDeleteView(DeleteView):
    model = Profissional
    template_name = 'profissional/profissional_confirm_delete'
    success_url = reverse_lazy('profissional-list')