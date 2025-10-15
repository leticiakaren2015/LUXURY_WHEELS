from django.db import models
from datetime import date, timedelta

# ---------------------------
# MODELO: CLIENTE
# ---------------------------
class Cliente(models.Model):
    CATEGORIAS = [
        ('Econômico', 'Econômico'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Econômico')

    def __str__(self):
        return f"{self.nome} ({self.categoria})"


# ---------------------------
# MODELO: VEÍCULO
# ---------------------------
class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"


# ---------------------------
# MODELO: FORMA DE PAGAMENTO
# ---------------------------
class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Forma de Pagamento"
        verbose_name_plural = "Formas de Pagamento"


# ---------------------------
# MODELO: RESERVA
# ---------------------------
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Função para calcular o valor total automaticamente
    def calcular_valor_total(self):
        dias = (self.data_fim - self.data_inicio).days + 1

        # Valores fixos conforme categoria
        precos = {
            'Econômico': 50,
            'Silver': 250,
            'Gold': 600,
        }

        valor_diaria = precos.get(self.cliente.categoria, 0)
        return dias * valor_diaria

    # Sobrescreve o save() para calcular automaticamente antes de salvar
    def save(self, *args, **kwargs):
        self.valor_total = self.calcular_valor_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva de {self.cliente.nome} - {self.veiculo.modelo}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
