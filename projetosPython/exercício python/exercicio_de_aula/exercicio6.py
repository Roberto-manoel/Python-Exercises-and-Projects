import requests
import concurrent.futures

def scrape_concurrent(url):
    try:
        response = requests.get(url)
        return response.content
    except:
        return None

# Lista de URLs a serem raspadas
urls = [
    "https://www.example.com/page1",
    "https://www.example.com/page2",
    "https://www.example.com/page3",
    "https://www.example.com/page4",
    "https://www.example.com/page5",
    "https://www.example.com/page6",
    "https://www.example.com/page7",
    "https://www.example.com/page8",
    "https://www.example.com/page9",
    "https://www.example.com/page10"
]

if __name__ == '__main__':
    # Utiliza o ThreadPoolExecutor para realizar scraping concorrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Mapeia a função scrape_concurrent para cada URL na lista
        results_concurrent = list(executor.map(scrape_concurrent, urls))

    # Imprime os resultados obtidos
    print(results_concurrent)