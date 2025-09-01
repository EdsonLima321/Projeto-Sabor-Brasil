from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroUsuarioForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro feito com sucesso!")
            return redirect('index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return render(request, 'usuarios/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('index')