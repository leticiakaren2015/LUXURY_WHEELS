from django.contrib import admin
from .models import Cliente, Veiculo, FormaPagamento, Reserva
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# ==============================
# Lista fixa de formas de pagamento
# ==============================
FORMA_DE_PAGAMENTO_FIXA = ['PIX', 'Dinheiro', 'Cartão de Crédito']


# ==============================
# Admin para Cliente
# ==============================
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'categoria')
    search_fields = ('nome', 'email')
    list_filter = ('categoria',)
    ordering = ('nome',)


# ==============================
# Admin para Veículo
# ==============================
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'placa', 'disponivel')
    list_filter = ('disponivel', 'marca')
    search_fields = ('marca', 'modelo', 'placa')
    ordering = ('marca', 'modelo')


# ==============================
# Admin para Forma de Pagamento (fixa)
# ==============================
@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    ordering = ('descricao',)

    # Bloqueia a adição manual
    def has_add_permission(self, request):
        return False

    # Mostra apenas as formas fixas
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(descricao__in=FORMA_DE_PAGAMENTO_FIXA)


# ==============================
# Admin para Reserva
# ==============================
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'veiculo', 'data_inicio', 'data_fim', 'forma_pagamento', 'valor_total')
    list_filter = ('data_inicio', 'data_fim', 'forma_pagamento')
    search_fields = ('cliente__nome', 'veiculo__modelo')
    ordering = ('data_inicio',)
    readonly_fields = ('valor_total',)  # Campo de valor total só leitura


# ==============================
# Criação automática das formas fixas após migrações
# ==============================
@receiver(post_migrate)
def criar_formas_pagamento_fixas(sender, **kwargs):
    if sender.name == 'luxurywares':  # 🔹 substitua pelo nome da sua app Django
        for descricao in FORMA_DE_PAGAMENTO_FIXA:
            FormaPagamento.objects.get_or_create(descricao=descricao)
    # Exclui qualquer outro registro que não esteja na lista fixa
    FormaPagamento.objects.exclude(descricao__in=FORMA_DE_PAGAMENTO_FIXA).delete()
