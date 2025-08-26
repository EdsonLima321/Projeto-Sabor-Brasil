from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def login(request):
    return render(request, 'usuarios/login.html')

def receita(request):
    return render(request, 'receita/feijoada.html')

