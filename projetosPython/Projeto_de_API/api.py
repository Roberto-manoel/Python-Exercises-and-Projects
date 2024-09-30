from flask import Flask, jsonify, request, abort

# Cria uma nova instância da aplicação Flask
app = Flask(__name__)

# Banco de dados simulado
users = {}    # Dicionário para armazenar dados do usuário
accounts = {} # Dicionário para armazenar dados da conta

# Define uma rota para a URL raiz que dá as boas-vindas aos usuários na API do Banco
@app.route('/')
def welcome():
    return "Welcome to the Bank API!"

# Define uma rota para listar todos os usuários
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(list(users.values()))

# Define uma rota para adicionar um novo usuário
@app.route('/user', methods=['POST'])
def add_user():
    user = request.json
    if 'id' not in user:
        abort(400, description="Missing user ID")
    users[user['id']] = user
    return jsonify(user), 201

# Define uma rota para obter um usuário específico pelo user_id
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    abort(404, description="User not found")

# Define uma rota para deletar um usuário específico pelo user_id
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return '', 204
    abort(404, description="User not found")

# Define uma rota para criar uma nova conta
@app.route('/account', methods=['POST'])
def create_account():
    account = request.json
    if 'user_id' not in account:
        abort(400, description="Missing user ID")
    if account['user_id'] not in users:
        abort(404, description="User not found")
    account_id = len(accounts) + 1
    accounts[account_id] = {'balance': 0, 'withdrawals': 0, 'user_id': account['user_id']}
    return jsonify({'account_id': account_id}), 201

# Define uma rota para depositar dinheiro em uma conta
@app.route('/account/<int:account_id>/deposit', methods=['POST'])
def deposit(account_id):
    if account_id not in accounts:
        abort(404, description="Account not found")
    amount = request.json.get('amount', 0)
    accounts[account_id]['balance'] += amount
    return jsonify({'balance': accounts[account_id]['balance']}), 200

# Define uma rota para sacar dinheiro de uma conta
@app.route('/account/<int:account_id>/withdraw', methods=['POST'])
def withdraw(account_id):
    if account_id not in accounts:
        abort(404, description="Account not found")
    amount = request.json.get('amount', 0)
    if accounts[account_id]['withdrawals'] >= 3:
        abort(400, description="Withdrawal limit reached")
    if accounts[account_id]['balance'] < amount:
        abort(400, description="Insufficient funds")
    accounts[account_id]['balance'] -= amount
    accounts[account_id]['withdrawals'] += 1
    return jsonify({'balance': accounts[account_id]['balance']}), 200

# Define uma rota para obter o extrato de uma conta
@app.route('/account/<int:account_id>/statement', methods=['GET'])
def statement(account_id):
    if account_id not in accounts:
        abort(404, description="Account not found")
    return jsonify(accounts[account_id])

# Define uma rota para deletar uma conta
@app.route('/account/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    if account_id not in accounts:
        abort(404, description="Account not found")
    if accounts[account_id]['balance'] > 0:
        abort(400, description="Account has balance")
    del accounts[account_id]
    return '', 204

# Executa a aplicação Flask se este script for executado como o programa principal
if __name__ == '__main__':
    app.run(debug=True)