from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def processa_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                'username': username,
                'password': password
            }
            messages.add_message(request=request, message='Usuário ou senha incorretos.', level=messages.ERROR)
            return render(request, 'autenticacao/login.html', context)

    return render(request, 'autenticacao/login.html')