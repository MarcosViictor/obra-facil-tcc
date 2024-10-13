# usuarios/urls.py
from django.urls import path
from .views.cadastro.cadastro_usuario import cadastrar_usuario  

urlpatterns = [
    path('cadastro/', cadastrar_usuario, name='cadastro'),
]
