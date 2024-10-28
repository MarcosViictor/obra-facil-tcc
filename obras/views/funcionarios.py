from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from obras.models import Profissional
from obras.forms.profissional_forms import ProfissionalForm  

class ProfissionalListView(ListView):
    model = Profissional
    template_name = 'profissional/profissional_list.html'
    context_object_name = 'profissionais'

class ProfissionalDetailView(DetailView):
    model = Profissional
    template_name = 'profissional/profissional_detail.html'
    context_object_name = 'profissionais'

class ProfissionalCreateView(CreateView):
    model = Profissional
    form_class = ProfissionalForm  # Altere esta linha
    template_name = 'profissional/profissional_form.html'
    success_url = reverse_lazy('profissional-list')

class ProfissionalUpdateView(UpdateView):
    model = Profissional
    form_class = ProfissionalForm  # Altere esta linha
    template_name = 'profissional/profissional_form.html'
    success_url = reverse_lazy('profissional-list')

class ProfissionalDeleteView(DeleteView):
    model = Profissional
    template_name = 'profissional/profissional_confirm_delete.html'
    success_url = reverse_lazy('profissional-list')