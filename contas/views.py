import re
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Perfil
from . usuario_form import PerfilForm, UserForm
from django.db import transaction
from django.template.loader import render_to_string

@transaction.atomic
def criar_conta(request):
    if request.method == 'POST':

        user = UserForm(request.POST)
        perfil = PerfilForm(request.POST, request.FILES)

        usr = User.objects.create_user(
            first_name=user.cleaned_data['first_name'],
            last_name=user.cleaned_data['last_name'],
            username=user.cleaned_data['username'],
            email=user.cleaned_data['email'],
            password=user.cleaned_data['password'],
        )

        perl = Perfil(bio=perfil.cleaned_data['bio'],
                      foto=perfil.cleaned_data['foto'],
                      user=usr)

        if perfil.is_valid() and user.is_valid():
            perl.save()
            return redirect('login')
        else:
            return render(request, 'contas/criar_conta.html', {'form': user, 'form_perfil': perfil})
    else:
        return render(request, 'contas/criar_conta.html', {'form': UserForm(), 'form_perfil': PerfilForm()})


def validou_email(email):

    #regex = '^(\w+)@[a-z]+(\.[a_z]+){1,2}$'
    regex = "^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$"

    if (re.search(regex, email)):
        return True
    else:
        return False


def htmx_valida_username(request):

    context = {'error_usrname': 'Usuário não disponível.', 'st_submit': 'disabled', 'cor': 'red'}
    usernameParam = request.POST.get('username')

    if not User.objects.filter(username=usernameParam):
        context['error_usrname'] = 'Usuário disponível.'
        context['cor'] = 'green'

    if PerfilForm(request.POST).is_valid():
        context['st_submit'] = ''

    str_template = render_to_string('contas/feedback_form_validation.html', context)
    return HttpResponse(str_template)


def htmx_valida_senha(request):

    context = {'error_pwd': 'As senhas não coincidem.', 'st_submit': 'disabled', 'cor': 'red'}

    pwd_confirm = request.POST.get('pwd_confirm')
    password = request.POST.get('password')

    if pwd_confirm == password and PerfilForm(request.POST).is_valid():
        context['error_pwd'] = ''
        context['st_submit'] = ''

    str_template = render_to_string('contas/feedback_form_validation.html', context)
    return HttpResponse(str_template)


def htmx_valida_email(request):

    context = { 'email_val': 'Email inválido ou já cadastrado', 'st_submit': 'disabled' }

    emailParam = request.POST.get('email')

    if not validou_email(emailParam):
        return HttpResponse('<label style="color:red;">Email inválido.</label>')

    if User.objects.filter(email=emailParam):
        return HttpResponse('<label style="color:red;">Email já cadastrado</label>')
    else:
        context['email_val'] = 'Email disponível e válido.'
        context['st_submit'] = ''
        str_template = render_to_string('contas/feedback_form_validation.html', context)
        return HttpResponse(str_template)