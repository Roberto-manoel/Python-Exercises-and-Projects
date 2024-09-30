import requests  # Importando o módulo requests para fazer solicitações HTTP
from bs4 import BeautifulSoup  # Importando o módulo BeautifulSoup para analisar o HTML
import re  # Importando o módulo re para trabalhar com expressões regulares

url = 'https://www.w3schools.io/file/yaml-sample-example/'  # URL do site que queremos raspar
response = requests.get(url)  # Fazendo uma solicitação GET para a URL
soup = BeautifulSoup(response.text, 'html.parser')  # Analisando o conteúdo HTML da resposta
yaml_example = soup.find('pre').text  # Obtendo o texto do elemento <pre> que contém o exemplo YAML

# Encontrando todos os comentários no exemplo YAML usando expressões regulares
comments = re.findall(r'#(.*)', yaml_example)

# Imprimindo cada comentário encontrado
for comment in comments:
    print(comment)

# Escrevendo o exemplo YAML em um arquivo chamado 'example.yaml'
with open('example.yaml', 'w') as file:
    file.write(yaml_example)