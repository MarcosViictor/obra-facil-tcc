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
            request.session['user_id'] = usuario.id
            return redirect('home')  
            return HttpResponse("Usuário ou senha inválidos.")
    
    return render(request, 'usuarios/login.html')
