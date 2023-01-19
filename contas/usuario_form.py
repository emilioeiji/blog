from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django import forms


class PerfilForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Ultimo Nome',
            'username': 'Nome de Usuário',
            'email': 'Endereço de Email',
            'password': 'Senha',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }