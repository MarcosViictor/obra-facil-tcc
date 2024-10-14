from django.urls import path, include  # Importe o include
from .views.cadastro.cadastro_usuario import cadastrar_usuario  
from .views.login.login_usuario import login_usuario

urlpatterns = [
    path('cadastro/', cadastrar_usuario, name='cadastro'),
    path('login/', login_usuario, name='login'),
    path('obras/', include('obras.urls')), 
]
