#Importando o módulo Flask para criar uma aplicação web 
from flask import Flask, request, jsonify
#Criando uma instância da classe Flask

app = Flask(__name__)
#Definindo uma rota para a API que aceita requisições POST

@app.route("/api", methods=["POST"])
def api():#Obtendo os dados enviados no corpo da requisição em formato JSON
    data = request.get_json()#Verificando se os dados são válidos e contêm os campos necessários
    if not data or "valor1" not in data or "valor2" not in data or "operacao" not in data:#Retornando uma resposta com código 400 (Bad Request) e uma mensagem de erro em formato JSON
        return jsonify({"erro": "Dados inválidos"}), 400#Atribuindo os valores dos campos a variáveis locais
    valor1 = data["valor1"]
    valor2 = data["valor2"]
    operacao = data["operacao"]#Verificando se os valores são números
    if not isinstance(valor1, (int, float)) or not isinstance(valor2, (int, float)):#Retornando uma resposta com código 400 (Bad Request) e uma mensagemde erro em formato JSON
        return jsonify({"erro": "Os valores devem ser números"}), 400#Verificando se a operação e uma das quatro operações básicas
    if operacao not in ["+", "-", "*", "/"]:#Retornando uma resposta com código 400 (Bad Request) e uma mensagem de erro em formato JSON
        return jsonify({"erro": "A operação deve ser uma das seguintes: +, -, *, /"}), 400#Realizando a operação de acordo com o símbolo informado
    if operacao == "+":
        resultado = valor1 + valor2
    elif operacao == "-":
        resultado = valor1 - valor2
    elif operacao == "*":
        resultado = valor1 * valor2
    elif operacao == "/":#Verificando se o divisor é diferente de zero
        if valor2 == 0:#Retornando uma resposta com código 400 (Bad Request) e uma mensagem de erro em formato JSON
            return jsonify({"erro": "Não é possível dividir por zero"}), 400
        resultado = valor1 / valor2
    else:#Retornando uma resposta com código 400 (Bad Request) e uma mensagem de erro em formato JSON
        return jsonify({"erro": "Operação inválida"}), 400#Retornando uma resposta com código 200 (OK) e o resultado da operação em formato JSON
    return jsonify({"resultado": resultado}), 200
#Executando a aplicação web se o script for executado diretamente
if __name__ == "__main__":
    app.run(debug=True)
#importando o módulo unittest para realizar teste automadizados
import unittest
import json
from flask import Flask
from api_mentorama import app
#Criando uma classe de teste que herda da classe TestCase domódulo unittest
class FlaskTestCase(unittest.TestCase):#Definindo um método que é executado antes de cada teste
    def setUp(self):#Criando um cliente de teste para simular requisições a aplicação web
        self.app = app.test_client()#Definindo um método de teste que verifica se a API funciona corretamente
    def test_api(self):#Criando um dicionário com os dados a serem enviados na requisição
        data = { "valor1": 10, "valor2": 5, "operacao": "+" }#Enviando uma requisição POST a rota /api com os dados em formato JSON e o tipo de conteúdo adequado
        response = self.app.post("/api", data=json.dumps(data), content_type="application/json")#Verificando se o código de status da resposta é 200(OK)
        self.assertEqual(response.status_code, 200)#Verificando se o resultado da operação na resposta é 15
        self.assertEqual(response.get_json()["resultado"], 15)#Executando os teste se o script for executado diretamente
    if __name__ == "__main__":
        unittest.main()
