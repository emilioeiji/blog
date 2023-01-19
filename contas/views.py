from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . usuario_form import PerfilForm

def criar_conta(request):
    if request.method == 'POST':
        profile = PerfilForm(request.POST)
        if profile.is_valid():
            usr = User.objects.create_user(
                first_name=profile.cleaned_data['first_name'],
                last_name=profile.cleaned_data['last_name'],
                username=profile.cleaned_data['username'],
                email=profile.cleaned_data['email'],
                password=profile.cleaned_data['password']
            )
            usr.save()
            return redirect('login')
        else:
            return render(request, 'contas/criar_conta.html', {'form': profile})
    else:
        return render(request, 'contas/criar_conta.html', {'form': PerfilForm})

    return render(request, 'contas/criar_conta.html')


def htmx_valida_username(request):
    usernameParam = request.POST.get('username')
    if len(usernameParam) <5 :
        return HttpResponse("<label style='color:red;'>Tamanho mínimo de 5 caracteres.</label>")
    elif User.objects.filter(username=usernameParam):
        return HttpResponse('<label style="color:red;">Usuário Indisponível</label>')
    else:
        return HttpResponse('<label style="color:green;">Usuário Disponível</label>')


def htmx_valida_senha(request):
    pwd_confirm = request.POST.get('pwd_confirm')
    password = request.POST.get('password')

    if pwd_confirm != password:
        return HttpResponse('<label style="color:red;">Senhas não são iguais.</label>')
    else:
        return HttpResponse('')
