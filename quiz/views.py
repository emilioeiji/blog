from django.http import HttpResponse
from django.shortcuts import render

from quiz.models import Questao


# Create your views here.
def get_quiz(request):
    questao = Questao.objects.get(pk=1)
    context = {
        'questao': questao
    }
    return render(request, 'quiz/quiz.html', context)

def get_resposta(request):
    resposta = request.POST.get('resposta')

    if resposta == 'True':
        return HttpResponse('<p style="color:green"> Resposta Correta!</p>')
    elif resposta == 'False':
        return HttpResponse('<p style="color:red"> Resposta Incorreta! </p>')
    else:
        return HttpResponse('<p style="color:yellow"> Selecione uma alternativa! </p>')
