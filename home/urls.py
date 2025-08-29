from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('receitas/', views.receitas, name='feijoada'),
    path('registrar/', views.registrar_usuario, name='registrar'),
]