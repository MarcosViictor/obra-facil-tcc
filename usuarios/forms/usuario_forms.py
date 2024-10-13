from django import forms
from django.contrib.auth.models import User
from usuarios.models import Perfil

class FormularioCadastroUsuario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirme sua senha')
    tipo_usuarios = forms.ChoiceField(choices=Perfil.TIPOS_USUARIOS, label='Tipo de Usuário')  
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('password')
        senha_confirm = cleaned_data.get('password_confirm')

        if senha and senha_confirm and senha != senha_confirm:
            raise forms.ValidationError('As senhas não são iguais')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
