from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPOS_USUARIOS = (
        ('gerente', 'Gerente'),
        ('mestre', 'Mestre')
    )

    usuarios = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuarios = models.CharField(max_length=10, choices=TIPOS_USUARIOS)
    
    # Relação para permitir que um gerente tenha vários mestres
    mestres = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='gerentes')

    def __str__(self):
        return f"{self.usuarios.username} ({self.get_tipo_usuarios_display()})"
