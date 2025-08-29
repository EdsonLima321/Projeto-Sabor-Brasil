from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('receitas/', views.receitas, name='feijoada'),
    path('login/', views.login, name='login'),
]