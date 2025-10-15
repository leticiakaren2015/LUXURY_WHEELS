from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Cliente, Veiculo, Reserva
from .forms import ClienteForm, VeiculoForm, ReservaForm

# ======================
# Home
# ======================
def home(request):
    return redirect('listar_reserva')  # redireciona para a lista de reservas

# ======================
# Clientes
# ======================
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/criar_cliente.html', {'form': form, 'editar': True})

def confirmar_excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/confirmar_excluir_cliente.html', {'cliente': cliente})

# ======================
# Veículos
# ======================
def listar_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/listar_veiculos.html', {'veiculos': veiculos})

def criar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/criar_veiculo.html', {'form': form})

def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculos/criar_veiculo.html', {'form': form, 'editar': True})

def confirmar_excluir_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_veiculos')
    return render(request, 'veiculos/confirmar_excluir_veiculo.html', {'veiculo': veiculo})

# ======================
# Reservas
# ======================
def listar_reservas(request):
    reservas = Reserva.objects.all().order_by('-data_inicio')
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  # o save() calcula valor_total automaticamente
            return redirect('listar_reserva')
    else:
        form = ReservaForm()
    return render(request, 'reservas/criar_reserva.html', {'form': form})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reserva')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/criar_reserva.html', {'form': form, 'editar': True})

def confirmar_excluir_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('listar_reserva')
    return render(request, 'reservas/confirmar_excluir_reserva.html', {'reserva': reserva})

# ======================
# Login do Usuário
# ======================

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')  # Admin vai pro painel
            else:
                return redirect('listar_reserva')  # Usuário comum vai pra reservas
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'usuarios/login.html')

# ======================
# Logout do Usuário
# ======================

def logout_usuario(request):
    logout(request)
    return redirect('login')

# ======================
# Registro de Usuário
# ======================

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Esse nome de usuário já existe.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
    return render(request, 'usuarios/registrar.html')


