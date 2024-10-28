from django.shortcuts import render, get_object_or_404
from obras.models import Obra, Acompanhamento

def dashboard_obra(request, obra_id):
    # Buscar a obra pelo ID
    obra = get_object_or_404(Obra, id=obra_id)
    
    # Coletar materiais e calcular o custo total
    materiais = obra.materiais.all()
    total_valor_materiais = sum(material.custo_total for material in materiais)
    
    # Coletar profissionais e calcular o total de salários
    profissionais = obra.profissionais.all()
    total_salario_profissionais = sum(profissional.salario for profissional in profissionais)
    
    # Calcular o saldo financeiro da obra
    total_custos = total_valor_materiais + total_salario_profissionais
    saldo_final = obra.valor_total - total_custos

    # Coletar acompanhamentos e progresso total
    acompanhamentos = obra.acompanhamentos.all()
    progresso_total = obra.progresso_total  # Assumindo que esse campo é atualizado automaticamente
    
    # Contexto para o template
    context = {
        'obra': obra,
        'materiais': materiais,
        'total_valor_materiais': total_valor_materiais,
        'profissionais': profissionais,
        'total_salario_profissionais': total_salario_profissionais,
        'valor_total_obra': obra.valor_total,
        'total_custos': total_custos,
        'saldo_final': saldo_final,
        'acompanhamentos': acompanhamentos,
        'progresso_total': progresso_total,
    }
    
    return render(request, 'obra/dashboard_obra.html', context)
