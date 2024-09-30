# Guia de Implementação da API Bancária

Este guia irá ajudá-lo a implementar o código Flask fornecido para uma API bancária simples.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:
- Python 3
- Flask

Você pode instalar o Flask usando o pip:

```bash
pip install flask
 
Copiar
Configuração
1. Salve o código Flask em um arquivo chamado app.py.
2. Abra o terminal e navegue até o diretório onde o arquivo app.py está localizado.
Execução
Para executar a aplicação, use o seguinte comando no terminal:
python app.py
Copiar
Isso iniciará um servidor local no endereço http://127.0.0.1:5000/, onde você poderá acessar a API.
Uso da API
A API possui várias rotas que permitem gerenciar usuários e contas bancárias:
• GET /: Uma mensagem de boas-vindas da API.
• GET /users: Lista todos os usuários.
• POST /user: Adiciona um novo usuário.
• GET /user/<user_id>: Obtém um usuário específico.
• DELETE /user/<user_id>: Deleta um usuário específico.
• POST /account: Cria uma nova conta.
• POST /account/<account_id>/deposit: Deposita dinheiro em uma conta.
• POST /account/<account_id>/withdraw: Saca dinheiro de uma conta.
• GET /account/<account_id>/statement: Obtém o extrato de uma conta.
• DELETE /account/<account_id>: Deleta uma conta.
Testando a API
Você pode testar a API usando ferramentas como Postman ou cURL para fazer requisições HTTP para as rotas definidas.