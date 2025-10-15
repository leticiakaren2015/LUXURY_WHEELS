from django.urls import path
from django.contrib import admin
from django.urls import include
from . import views

urlpatterns = [
    # ======================
    # Rotas de Cliente
    # ======================
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/criar/', views.criar_cliente, name='criar_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:id>/', views.confirmar_excluir_cliente, name='confirmar_excluir_cliente'),

    # ======================
    # Rotas de Veículo
    # ======================
    path('veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('veiculos/criar/', views.criar_veiculo, name='criar_veiculo'),
    path('veiculos/editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),
    path('veiculos/excluir/<int:id>/', views.confirmar_excluir_veiculo, name='confirmar_excluir_veiculo'),

    # ======================
    # Rotas de Reserva
    # ======================
    path('reservas/', views.listar_reservas, name='listar_reserva'),
    path('reservas/criar/', views.criar_reserva, name='criar_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/excluir/<int:id>/', views.confirmar_excluir_reserva, name='excluir_reserva'),

    # ======================
    # Home (página inicial)
    # ======================
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # ======================
    # Rotas de Usuário (Login, Logout, Registro)
    # ======================
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('registrar/', views.registrar_usuario, name='registrar'),

]
