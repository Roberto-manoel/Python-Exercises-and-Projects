from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import google.generativeai as genai

# Substitua 'YOUR_API_KEY' pela sua chave de API do Google Cloud
API_KEY = 'YOUR_API_KEY'

# Substitua 'YOUR_CSE_ID' pelo seu ID de mecanismo de pesquisa personalizado
CSE_ID = 'YOUR_CSE_ID'

# Configuração da biblioteca google-generativeai
genai.configure(api_key=API_KEY)

# Configuração do modelo
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Inicialização do modelo
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def index(request):
    # Renderiza o template principal do chatbot
    return render(request, 'chat/chat.html')

@csrf_exempt
def get_response(request):
    # Esta view lida com as mensagens enviadas ao chatbot
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_query = data['query']

            # Inicia um chat com o modelo
            convo = model.start_chat(history=[])

            # Envia uma mensagem para o modelo e obtém a resposta
            convo.send_message(user_query)
            chatbot_response = convo.last.text

            # Valida se a resposta está vazia
            if chatbot_response:
                return JsonResponse({'response': chatbot_response})
            else:
                return JsonResponse({'error': 'Resposta vazia da API do Google Studio'}, status=500)

        except Exception as e:
            # Manipula exceções de forma genérica
            print(f"Erro ao processar a requisição: {e}")
            return JsonResponse({'error': 'Ocorreu um erro durante o processamento da requisição'}, status=500)

    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)