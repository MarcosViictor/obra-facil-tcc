from django.db import models
from usuarios.models import Perfil

class Obra(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.CharField(max_length=50)
    data_inicio = models.DateField()
    dt_prev_fim = models.DateField()
    progresso_total = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Progresso total da obra em %")
    gerente = models.ForeignKey(
        Perfil, on_delete=models.CASCADE, related_name='obras_gerenciadas',
        limit_choices_to={'tipo_usuarios': 'gerente'}  
    )
    mestres = models.ManyToManyField(
        Perfil, related_name='obras_como_mestre', blank=True,
        limit_choices_to={'tipo_usuarios': 'mestre'} 
    )

    def __str__(self):
        return self.nome

    def atualizar_progresso_total(self):
        acompanhamentos = self.acompanhamentos.all()
        if acompanhamentos.exists():
            total_progresso = sum(acomp.progresso for acomp in acompanhamentos)
            self.progresso_total = total_progresso / acompanhamentos.count()
            self.save()
class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=50) 
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='profissionais')

    def __str__(self):
        return f"{self.nome} - {self.funcao}"

class Acompanhamento(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='acompanhamentos')
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    progresso = models.DecimalField(max_digits=5, decimal_places=2, help_text="Progresso em %")
    mestre_responsavel = models.ForeignKey(
        Perfil, on_delete=models.CASCADE, related_name='acompanhamentos',
        limit_choices_to={'tipo_usuarios': 'mestre'}
    )

    def __str__(self):
        return f"Acompanhamento em {self.obra.nome} - {self.data} - {self.progresso}%"

from django.db import models

class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantidade do material")
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço unitário do material")
    data_compra = models.DateField()
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='materiais')
    fornecedor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades"

    @property
    def custo_total(self):
        return self.quantidade * self.preco_unitario
