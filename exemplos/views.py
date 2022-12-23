from django.shortcuts import render


def bootstrap(request):
    return render(request, 'exemplos/containers.html')