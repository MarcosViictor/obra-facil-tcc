from django.db import models
from django.urls import reverse
from usuarios.models import Perfil

class Obra(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.CharField(max_length=50)
    data_inicio = models.DateField()
    dt_prev_fim = models.DateField()
    progresso_total = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Progresso total da obra em %")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, help_text="Valor total da obra", default=0)
    valor_gasto = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Valor gasto em materiais")
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
        total_progresso = sum(acomp.progresso for acomp in self.acompanhamentos.all())
        if total_progresso > 100:
            total_progresso = 100  # Para garantir que o progresso total não ultrapasse 100%
        self.progresso_total = total_progresso
        self.save()

    def atualizar_valor_gasto(self):
        total_gasto = sum(material.custo_total for material in self.materiais.all())
        self.valor_gasto = total_gasto
        self.save()

    @property
    def lucro(self):
        """Calcula o lucro com base no valor total e o valor gasto em materiais."""
        return self.valor_total - self.valor_gasto

    def get_absolute_url(self):
        return reverse('obra-detail', args=[self.pk])

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

    def save(self, *args, **kwargs):
        total_progresso_existente = sum(acomp.progresso for acomp in self.obra.acompanhamentos.all())
        if total_progresso_existente + self.progresso > 100:
            raise ValueError("O progresso total da obra não pode exceder 100%.")
        super().save(*args, **kwargs)
        self.obra.atualizar_progresso_total()

    def get_absolute_url(self):
        return reverse('acompanhamento-detail', args=[self.pk])

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='profissionais')

    def __str__(self):
        return f"{self.nome} - {self.funcao}"

    def get_absolute_url(self):
        return reverse('profissional-detail', args=[self.pk])

class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(help_text="Quantidade comprada")
    quantidade_consumida = models.IntegerField(default=0, help_text="Quantidade consumida")
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço unitário do material")
    data_compra = models.DateField()
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='materiais')
    fornecedor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades"

    @property
    def custo_total(self):
        """Calcula o custo total dos materiais comprados."""
        return self.quantidade * self.preco_unitario

    @property
    def quantidade_disponivel(self):
        """Calcula a quantidade de material disponível, subtraindo o consumido."""
        return self.quantidade - self.quantidade_consumida

    def save(self, *args, **kwargs):
        """Atualiza o valor gasto na obra sempre que o material for salvo."""
        super().save(*args, **kwargs)
        self.obra.atualizar_valor_gasto()

    def get_absolute_url(self):
        return reverse('material-detail', args=[self.pk])
