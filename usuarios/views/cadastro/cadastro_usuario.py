from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.forms.usuario_forms import FormularioCadastroUsuario
from usuarios.models import Perfil
from django.contrib.auth import login
from django.urls import reverse  # Import para redirecionamento

def cadastrar_usuario(request):
    if request.method == 'POST':
        formulario = FormularioCadastroUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            tipo_usuario = formulario.cleaned_data['tipo_usuarios'] 
            Perfil.objects.create(usuarios=usuario, tipo_usuarios=tipo_usuario)

            login(request, usuario)  # Loga o usuário automaticamente após cadastro
            return redirect(reverse('obra-list'))  # Redireciona para obra-list
    else:
        formulario = FormularioCadastroUsuario()

    return render(request, 'usuarios/cadastro.html', {'formulario': formulario})
