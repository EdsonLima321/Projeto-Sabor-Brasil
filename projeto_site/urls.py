from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('usuarios/', include('app_cadastro.urls')),
    path('categorias/', include('categorias.urls')),
    path('receitas/', include('receitas.urls')),
    path('admin/', admin.site.urls),
]