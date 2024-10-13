from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Adicione isso
]


