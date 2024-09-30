"""
Esse código é um exemplo de como usar a regressão linear para prever os preços de imóveis com base em diferentes variáveis. Vou explicar as etapas do código:
1. 
Importar bibliotecas: O código começa importando algumas bibliotecas necessárias, como pandas para manipulação de dados, sklearn para modelos de aprendizado de máquina e matplotlib para visualização de dados.
2. 
Carregar os dados: O código carrega os dados de um arquivo CSV chamado 'Housing.csv' em um DataFrame do pandas chamado 'df'.
3. 
Remover valores ausentes: O código remove qualquer linha que contenha valores ausentes no DataFrame.
4. 
Converter variáveis categóricas em numéricas: O código mapeia variáveis categóricas ('mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning' e 'prefarea') de 'yes'/'no' para 1/0, respectivamente.
5. 
Separar as variáveis independentes e dependentes: O código divide o DataFrame em duas partes: X contendo as variáveis independentes ('area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking' e 'prefarea') e y contendo a variável dependente ('price').
6. 
Separar os dados em conjuntos de treinamento e teste: O código divide os dados em conjuntos de treinamento e teste usando a função train_test_split do sklearn. Ele usa 80% dos dados para treinamento e 20% para teste.
7. 
Normalizar os dados de treinamento: Os dados de treinamento são normalizados subtraindo a média e dividindo pelo desvio padrão de cada variável.
8. 
Treinar o modelo de regressão linear: O código cria uma instância do modelo de regressão linear e o treina usando os dados de treinamento normalizados.
9. 
Normalizar os dados de teste: Os dados de teste são normalizados usando a mesma média e desvio padrão dos dados de treinamento.
10. 
Fazer previsões usando os dados de teste: O modelo treinado é usado para fazer previsões nos dados de teste normalizados.
11. 
Calcular as métricas de avaliação: O código calcula três métricas de avaliação para o modelo: R-quadrado (r2_score), MAE (mean_absolute_error) e MSE (mean_squared_error) usando os valores reais de y_test e as previsões y_pred.
12. 
Plotar os valores reais e previstos: O código cria um gráfico de dispersão para visualizar os valores reais (y_test) em relação aos valores previstos (y_pred).
13. 
Imprimir as métricas de avaliação: O código imprime as métricas de avaliação para o modelo, tanto para os dados de treinamento quanto para os dados de teste.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Carrega os dados em um DataFrame
df = pd.read_csv('Housing.csv')

# Remove valores ausentes
df = df.dropna()

# Converte variáveis categóricas em numéricas
df['mainroad'] = df['mainroad'].map({'yes': 1, 'no': 0})
df['guestroom'] = df['guestroom'].map({'yes': 1, 'no': 0})
df['basement'] = df['basement'].map({'yes': 1, 'no': 0})
df['hotwaterheating'] = df['hotwaterheating'].map({'yes': 1, 'no': 0})
df['airconditioning'] = df['airconditioning'].map({'yes': 1, 'no': 0})
df['prefarea'] = df['prefarea'].map({'yes': 1, 'no': 0})

# Separa as variáveis independentes e dependentes
X = df[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea']]
y = df['price']

# Separa os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normaliza os dados de treinamento
mean = X_train.mean()
std = X_train.std()
X_train = (X_train - mean) / std

# Treina o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Normaliza os dados de teste usando a mesma média e desvio padrão
X_test = (X_test - mean) / std

# Faz as previsões usando os dados de teste
y_pred = model.predict(X_test)

# Calcula o R-quadrado para os dados de teste
r2_test = r2_score(y_test, y_pred)

# Calcula o MAE para os dados de teste
mae_test = mean_absolute_error(y_test, y_pred)

# Calcula o MSE para os dados de teste
mse_test = mean_squared_error(y_test, y_pred)

# Plot dos valores reais e previstos
plt.scatter(y_test, y_pred)
plt.xlabel('Valores Reais')
plt.ylabel('Valores Previstos')
plt.title('Valores Reais vs Valores Previstos')
plt.show()

print('R-quadrado (treinamento):', model.score(X_train, y_train))
print('R-quadrado (teste):', r2_test)
print('MAE (treinamento):', mean_absolute_error(y_train, model.predict(X_train)))
print('MAE (teste):', mae_test)
print('MSE (treinamento):', mean_squared_error(y_train, model.predict(X_train)))
print('MSE (teste):', mse_test)
