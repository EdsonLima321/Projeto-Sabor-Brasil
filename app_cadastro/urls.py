from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]