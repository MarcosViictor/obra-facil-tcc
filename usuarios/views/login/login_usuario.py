from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            # Redireciona para a página de lista de obras após login bem-sucedido
            return redirect('obra-list')  # 'obra-list' deve ser o nome da sua URL
        else:
            return HttpResponse("Usuário ou senha inválidos.")
    
    return render(request, 'usuarios/login.html')
