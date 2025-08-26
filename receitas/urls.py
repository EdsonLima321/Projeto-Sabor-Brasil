from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('receitas/', views.receita, name='feijoada'),
    # path('login/', views.login, name='login'),
    # # path('usuarios/', views.usuarios, name='listagem_usuarios'),
    # path('cadastro/', views.cadastro, name='cadastro'),
    # path('logout/', views.logout_view, name='logout'),
]