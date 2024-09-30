import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Python'

def getlinks(url):
    # Faz uma requisição GET para a URL especificada
    response = requests.get(url)

    # Cria um objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Imprime o título da página principal
    print(f'Página principal: {soup.title.string}')

    # Itera por todos os elementos 'a' na página
    for link in soup.find_all('a'):
        # Obtém o atributo 'href' de cada elemento 'a'
        href = link.get('href')

        # Verifica se o atributo 'href' existe e se começa com '/wiki/'
        if href and href.startswith('/wiki/'):
            # Cria uma nova URL usando o atributo 'href' encontrado
            newurl = f'https://pt.wikipedia.org{href}'
            # Imprime a URL da página secundária
            print(f'Página secundária: {newurl}')

# Chama a função getlinks com a URL especificada
getlinks(url)