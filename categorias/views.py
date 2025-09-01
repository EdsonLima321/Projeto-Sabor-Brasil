from django.shortcuts import render

def categorias(request):
    return render(request, 'categorias/categoria.html')

def index(request):
    return render(request, 'index.html')