from django.shortcuts import render, redirect
from app_cadastro.forms import RegistroUsuarioForm

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request,'usuarios/login.html')

def receitas(request):
    return render(request, 'feijoada.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'app_cadastro/registro.html', {'form': form})