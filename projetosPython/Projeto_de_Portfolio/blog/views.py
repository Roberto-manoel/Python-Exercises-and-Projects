from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Postagem, Comentario
from .forms import CommentForm
from django.shortcuts import get_object_or_404
import logging
logger = logging.getLogger(__name__)
from django.contrib import messages
from decouple import config
import requests
from django.http import JsonResponse
YOUTUBE_API_KEY = config('YOUTUBE_API_KEY')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('postagem_list')
            else:
                messages.error(request, 'Erro na autenticação do usuário.')
        return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('postagem_list')
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

# Adicionando a função de view para logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

def post_list(request):
    postagens = Postagem.objects.all()
    return render(request, 'blog/post_list.html', {'postagens': postagens})

@login_required
def post_detail(request, pk):
    logger.info("Usuário autenticado: %s", request.user.is_authenticated)
    postagem = get_object_or_404(Postagem, pk=pk)
    comentarios = Comentario.objects.filter(postagem=postagem)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.postagem = postagem
            comentario.usuario = request.user
            comentario.save()
            logger.info("Comentário salvo: %s", comentario.conteudo)
            return redirect('postagem_detail', pk=postagem.pk)
        else:
            logger.warning("Formulário inválido")
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'postagem': postagem, 'comentarios': comentarios, 'form': form})

def get_youtube_videos(request):
    base_youtube_api_url = "https://www.googleapis.com/youtube/v3"
    channel_id = "UC8_hfVPkdYi7UiIaFCkjPLQ"

    # Fazendo a requisição para a API do YouTube
    response = requests.get(
        f"{base_youtube_api_url}/search?key={YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=20"
    )

    # Verificando se a requisição foi bem sucedida
    if response.status_code == 200:
        videos = response.json().get('items', [])
        return render(request, 'blog/youtube_videos.html', {'videos': videos})
    else:
        return render(request, 'blog/error.html', {'message': "Não foi possível obter os vídeos do YouTube"})
