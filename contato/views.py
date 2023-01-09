from django.shortcuts import render
from contato.contato_form import FormContato


def contato(request):
    return render(request, 'contato/contato.html', {'form': FormContato()})


def processa_contato(request):
    return render(request, 'contato/contato.html', {'form': FormContato()})
