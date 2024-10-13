from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, response

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(request, username = username, password = password)

        if usuario is not None:
            login(request, usuario)
            perfil = usuario.perfil
            return HttpResponse(f"Login bem-sucedido! Você é um {perfil.get_tipo_usuarios_display()}.")
        else:
            return HttpResponse("Usuário ou senha inválidos.")
    return render(request, 'usuarios/login.html')
