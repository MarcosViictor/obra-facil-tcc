from django.views.generic import ListView
from obras.models import Obra

class DashboardView(ListView):
    model = Obra
    template_name = 'acompanhamento/dashboard.html'
    context_object_name = 'obras'
