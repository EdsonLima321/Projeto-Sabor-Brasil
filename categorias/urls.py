from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categorias, name='categoria'),
    path('home/', views.index, name='home'),
]