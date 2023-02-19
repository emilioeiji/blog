from django.shortcuts import render

# Create your views here.
def get_quiz(request):
    return render(request, 'quiz/quiz.html')