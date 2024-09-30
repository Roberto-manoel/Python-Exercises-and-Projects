import requests
from django.shortcuts import render
import os
from dotenv import load_dotenv
load_dotenv()

def get_home(request):
    return render(request, 'pages/home.html', {})

def get_site(request):
    return render(request, 'pages/index.html', {})

def get_redes_sociais(request):
    return render(request, 'pages/redes-sociais.html', {})

def get_tech_news(request):
    api_key = os.environ.get('NEWS_API_KEY')
    query = request.GET.get('q', '')

    # Se nenhuma consulta for fornecida, busque as principais manchetes
    if query == '':
        response = requests.get(f'https://newsapi.org/v2/top-headlines?country=br&apiKey={api_key}')
    else:
        response = requests.get(f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}')

    data = response.json()
    articles = data.get('articles', [])
    context = {'articles': articles}
    return render(request, 'pages/tech_news.html', context)
