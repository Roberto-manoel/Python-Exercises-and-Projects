"""
Esse código mostra um exemplo de uso de algoritmos de aprendizado de máquina para prever dados de saúde do sono e estilo de vida. Ele carrega um arquivo CSV, verifica a existência de uma coluna específica e realiza diferentes etapas dependendo disso.
Se a coluna existe, o código trata as variáveis categóricas, divide os dados em conjuntos de treinamento e teste e treina um modelo de classificação Random Forest. Ele faz previsões para os dados de teste e calcula a acurácia do modelo. Além disso, realiza uma previsão específica e imprime a acurácia e a previsão de distúrbio do sono.
Se a coluna não existe, o código imprime uma mensagem indicando isso.
Em seguida, o código seleciona colunas específicas para um modelo de regressão linear. Ele converte os valores para numéricos, remove linhas com valores não numéricos e treina o modelo de regressão linear.
O código faz previsões usando o modelo de regressão linear e avalia-o calculando o erro médio quadrático (MSE) e o coeficiente de determinação (R²). Também plota os dados de treinamento e a linha de regressão.
Por fim, são impressas previsões, métricas de avaliação e resultados para diferentes idades usando o modelo de regressão linear.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

# Carregando os dados do arquivo CSV
data_rf = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

# Verificando se a coluna 'Profession' existe no DataFrame
if 'Profession' in data_rf.columns:
    # Tratamento de variáveis categóricas
    data_rf = pd.get_dummies(data_rf, columns=['Gender', 'Profession', 'BMI Category'])

    # Dividindo os dados em conjuntos de treinamento e teste para o modelo Random Forest
    X_rf = data_rf.drop('Sleep Disorder', axis=1)
    y_rf = data_rf['Sleep Disorder']
    X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X_rf, y_rf, test_size=0.25)

    # Criando uma instância do modelo de classificação Random Forest
    model_rf = RandomForestClassifier()

    # Treinando o modelo Random Forest com os dados de treinamento
    model_rf.fit(X_train_rf, y_train_rf)

    # Fazendo previsões para os dados de teste com o modelo Random Forest
    predictions_rf = model_rf.predict(X_test_rf)

    # Calculando a acurácia do modelo Random Forest
    accuracy_rf = accuracy_score(y_test_rf, predictions_rf)
    print('Acurácia do Modelo Random Forest:', accuracy_rf)

    # Fazendo previsões para um exemplo específico com o modelo Random Forest
    example_rf = [[1, 27, 6, 6.1, 42, 'Male', 'Overweight', '126/83', 77, 4200, None]]
    prediction_rf = model_rf.predict(example_rf)
    print('Exemplo Random Forest:', example_rf)
    print('Previsão de Distúrbio do Sono Random Forest:', prediction_rf[0])
    print()
else:
    print("A coluna 'Profession' não existe no DataFrame.")

# Dividindo os dados em conjuntos de treinamento e teste para o modelo de Regressão Linear
X_lr = data_rf[['Age']]
y_lr = data_rf['Sleep Duration']

# Verificando o tipo de dados da coluna 'Sleep Duration'
print(data_rf['Sleep Duration'].dtype)

# Convertendo os valores para numéricos
data_rf['Sleep Duration'] = pd.to_numeric(data_rf['Sleep Duration'], errors='coerce')

# Removendo as linhas com valores não numéricos (NaN)
data_rf = data_rf.dropna(subset=['Sleep Duration'])

# Atualizando os conjuntos de treinamento e teste
X_lr = data_rf[['Age']]
y_lr = data_rf['Sleep Duration']
X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.25)

# Criando um modelo de regressão linear
model_lr = LinearRegression()

# Treinando o modelo de regressão linear no conjunto de treinamento
model_lr.fit(X_train_lr, y_train_lr)

# Fazendo uma previsão para uma pessoa com 40 anos usando o modelo de regressão linear
prediction_lr = model_lr.predict([[40]])

# Avaliando o modelo de regressão linear no conjunto de teste
predictions_test_lr = model_lr.predict(X_test_lr)
mse_lr = mean_squared_error(y_test_lr, predictions_test_lr)
r2_lr = r2_score(y_test_lr, predictions_test_lr)

# Plotando os dados e a linha de regressão usando o modelo de regressão linear
plt.scatter(X_train_lr, y_train_lr, color='blue')
plt.plot(X_train_lr, model_lr.predict(X_train_lr), color='red')
plt.xlabel('Idade')
plt.ylabel('Duração do Sono')
plt.show()

# Imprimindo a previsão do modelo de regressão linear
print('Previsão de Duração do Sono para uma pessoa de 40 anos:', prediction_lr)

# Imprimindo métricas de avaliação do modelo de regressão linear
print('Erro Médio Quadrático (MSE) do Modelo de Regressão Linear:', mse_lr)
print('Coeficiente de Determinação (R²) do Modelo de Regressão Linear:', r2_lr)

# Fazendo previsões para todas as idades usando o modelo de regressão linear
predictions_all_lr = model_lr.predict(pd.DataFrame({'Age': range(18, 80)}))
for age_lr, prediction_lr in zip(range(18, 80), predictions_all_lr):
    print('Idade:', age_lr, 'Duração do sono prevista pelo Modelo de Regressão Linear:', prediction_lr)