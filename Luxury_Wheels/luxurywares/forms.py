from django import forms
from .models import Reserva, Cliente, Veiculo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'categoria']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'placa', 'disponivel']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'veiculo', 'data_inicio', 'data_fim', 'forma_pagamento', 'valor_total']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'valor_total': forms.NumberInput(attrs={'readonly': 'readonly'}),  # campo só leitura
        }
