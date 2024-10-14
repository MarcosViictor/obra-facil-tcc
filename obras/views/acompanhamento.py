from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from obras.models import Acompanhamento, Obra

class AcompanhamentoListView(ListView):
    model = Acompanhamento
    template_name = 'acompanhamento/acompanhamento_list.html'
    context_object_name = 'acompanhamentos'

class AcompanhamentoDetailView(DetailView):
    model = Acompanhamento
    template_name = 'acompanhamento/acompanhamento_detail.html'

class AcompanhamentoCreateView(CreateView):
    model = Acompanhamento
    fields = ['obra', 'descricao', 'progresso', 'mestre_responsavel']
    template_name = 'acompanhamento/acompanhamento_form.html'

    def form_valid(self, form):
        acompanhamento = form.save(commit=False)
        obra = get_object_or_404(Obra, pk=acompanhamento.obra.pk)

        # Salva o acompanhamento e atualiza o progresso da obra
        acompanhamento.save()
        obra.atualizar_progresso_total()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('acompanhamento-list')

class AcompanhamentoUpdateView(UpdateView):
    model = Acompanhamento
    fields = ['obra', 'descricao', 'mestre_responsavel']
    template_name = 'acompanhamento/acompanhamento_form.html'

    def get_success_url(self):
        return reverse_lazy('acompanhamento-list')

class AcompanhamentoDeleteView(DeleteView):
    model = Acompanhamento
    template_name = 'acompanhamento/acompanhamento_confirm_delete.html'
    success_url = reverse_lazy('acompanhamento-list')
