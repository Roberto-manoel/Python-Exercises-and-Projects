# Chatbot Interativo

Este repositório contém o código-fonte de um chatbot interativo que utiliza tecnologias web modernas e uma API de inteligência artificial para responder às perguntas dos usuários.

## Frontend

O frontend é construído com HTML, Bootstrap e jQuery. Ele apresenta uma interface de usuário simples onde as mensagens podem ser digitadas e enviadas ao chatbot, e as respostas são exibidas na tela.

### Estrutura HTML

A estrutura HTML consiste em um cabeçalho que introduz o chatbot e uma caixa de chat onde as mensagens são exibidas. Há também um formulário com um campo de entrada para digitar as mensagens e um botão para enviá-las.

### jQuery e AJAX

O script jQuery é responsável por capturar o evento de envio do formulário, prevenir o comportamento padrão de recarregar a página, coletar a mensagem digitada pelo usuário e enviar uma solicitação AJAX para o servidor.

Quando a resposta é recebida do servidor, ela é exibida na caixa de chat. Se ocorrer um erro, uma mensagem de erro é exibida.

## Backend

O backend é implementado usando o framework Django do Python. Ele inclui uma view que lida com as solicitações AJAX enviadas pelo frontend e interage com uma API de inteligência artificial para obter respostas para as perguntas dos usuários.

### Django Views

A view get_response é uma função que espera solicitações POST com a mensagem do usuário em formato JSON. Ela processa a mensagem, interage com a API de inteligência artificial e retorna a resposta em formato JSON.

### Configuração da API de Inteligência Artificial

O código inclui a configuração para a biblioteca google-generativeai, que é usada para comunicar-se com a API de inteligência artificial. As configurações de segurança são definidas para evitar respostas prejudiciais.

## Configuração e Uso

Para usar este chatbot, você precisará substituir 'YOUR_API_KEY' e 'YOUR_CSE_ID' pelos valores apropriados fornecidos pelo Google Cloud.

Após configurar as chaves de API, você pode iniciar o servidor Django e acessar o frontend para começar a interagir com o chatbot.

---

Este README fornece uma visão geral do projeto e instruções básicas para configuração e uso. Para mais detalhes, consulte os comentários no código-fonte.