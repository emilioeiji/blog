from django.shortcuts import render
from . usuario_form import PerfilForm

def criar_conta(request):
    if request.method == 'POST':
        profile = PerfilForm(request.POST)
        if profile.is_valid():
            print("Formulário válido")
        else:
            print("Formulário inválido")
    else:
        return render(request, 'contas/criar_conta.html', {'form': PerfilForm})

    return render(request, 'contas/criar_conta.html')
