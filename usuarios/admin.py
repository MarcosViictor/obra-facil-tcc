from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuarios', 'tipo_usuarios')  # Usar os campos corretos

admin.site.register(Perfil, PerfilAdmin)
