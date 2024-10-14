from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Inclui as URLs do app `usuarios`
    path('obras/', include('obras.urls')),

    # Redireciona a URL base "/" para "/usuarios/login/"
    path('', lambda request: redirect('login')),
]
