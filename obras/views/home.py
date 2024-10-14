from django.shortcuts import render
from obras.models import Obra, Profissional, Material, Acompanhamento

def home(request):
    total_obras = Obra.objects.count()
    total_profissionais = Profissional.objects.count()
    total_materiais = Material.objects.count()
    obras_recentes = Obra.objects.order_by('-id')[:5]
    acompanhamentos_recentes = Acompanhamento.objects.order_by('-id')[:5]
    
    context = {
        'total_obras': total_obras,
        'total_profissionais': total_profissionais,
        'total_materiais': total_materiais,
        'obras_recentes': obras_recentes,
        'acompanhamentos_recentes': acompanhamentos_recentes,
    }
    return render(request, 'obra/home.html', context)
