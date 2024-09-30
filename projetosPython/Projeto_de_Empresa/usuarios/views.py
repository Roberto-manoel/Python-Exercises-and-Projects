from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres.')
            return redirect('/usuarios/cadastro')
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário já existe.')
            return redirect('/usuarios/cadastro')
        
        try:
            user = User.objects.create_user(
                username=username,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso.')
            return redirect('/usuarios/login')
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro interno do sistema: {e}')
            return redirect('/usuarios/cadastro')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)
        if user:
            auth_login(request, user)
            return redirect('/usuarios/home')
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos.')
        return redirect('/usuarios/login')

def home(request):
    return render(request, 'home.html')
