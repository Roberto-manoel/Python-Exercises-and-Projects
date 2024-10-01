# Sistema Bancário

Este projeto é um sistema bancário simples implementado em Python. Ele permite a criação de clientes, contas e a realização de transações como saques e depósitos.

## Estrutura do Projeto

### Classes Principais

- **Cliente**: Representa um cliente do banco, que possui um endereço e uma lista de contas.
- **PessoaFisica**: Subclasse de `Cliente` que adiciona informações específicas de uma pessoa física, como nome, data de nascimento e CPF.
- **Conta**: Representa uma conta bancária genérica com número, cliente, saldo, agência e histórico de transações.
- **ContaCorrente**: Subclasse de `Conta` que adiciona funcionalidades específicas de uma conta corrente, como limite de saque e número máximo de saques.

### Métodos Principais

- **Cliente**
  - `realizar_transacao(conta, transacao)`: Realiza uma transação na conta fornecida.
  - `adicionar_conta(conta)`: Adiciona uma conta à lista de contas do cliente.

- **Conta**
  - `sacar(valor)`: Realiza um saque da conta se o valor for menor ou igual ao saldo.
  - `depositar(valor)`: Realiza um depósito na conta se o valor for maior que zero.

- **ContaCorrente**
  - `sacar(valor)`: Realiza um saque da conta se o valor for menor ou igual ao saldo e ao limite, e se o número de saques for menor que o limite de saques.

## Exemplo de Uso

```python
from datetime import datetime

# Criação de um cliente Pessoa Física
cliente = PessoaFisica(nome="João Silva", data_nascimento=datetime(1990, 5, 20), cpf="123.456.789-00", endereco="Rua A, 123")

# Criação de uma conta corrente para o cliente
conta_corrente = ContaCorrente.nova_conta(cliente, numero="0001")

# Adiciona a conta ao cliente
cliente.adicionar_conta(conta_corrente)

# Realiza um depósito
conta_corrente.depositar(1000)

# Realiza um saque
conta_corrente.sacar(200)
 
Copiar
Requisitos
• Python 3.6 ou superior
Como Executar
Navegue até o diretório do projeto:
cd sistema-bancario
Copiar
3. Execute o script principal:
python main.py
Copiar
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.