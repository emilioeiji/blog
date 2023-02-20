from django.shortcuts import render

from quiz.models import Questao


# Create your views here.
def get_quiz(request):
    questao = Questao.objects.get(pk=1)
    context = {
        'questao': questao
    }
    return render(request, 'quiz/quiz.html', context)