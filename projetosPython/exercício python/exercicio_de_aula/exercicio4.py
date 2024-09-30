import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Carregando o conjunto de dados
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
colunas = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataset = pd.read_csv(url, names=colunas, skiprows=0, delimiter="")

# Imprimindo informações sobre o conjunto de dados
print(dataset.shape)  # imprime o formato do conjunto de dados (linhas, colunas)
print(dataset.dtypes)  # imprime os tipos de dados de cada coluna
print(dataset.head())  # imprime as primeiras linhas do conjunto de dados

# Dividindo o conjunto de dados em atributos (X) e variável alvo (Y)
array = dataset.values
X = array[:, 0:8].astype(float)
Y = array[:, 8]

# Dividindo os dados em conjuntos de treinamento e teste
test_size = 0.20
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# Configurando a validação cruzada
num_folds = 10
scoring = 'accuracy'

# Definindo os modelos a serem avaliados
models = []
models.append(('LR', LogisticRegression(solver='newton-cg')))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('MB', GaussianNB()))
models.append(('SVM', SVC()))

results = []
names = []

# Avaliando cada modelo utilizando validação cruzada
for name, model in models:
    kfold = KFold(n_splits=num_folds)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# Plotando um gráfico comparativo dos modelos
fig = plt.figure()
fig.suptitle("Comparação dos Modelos")
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

# Avaliando modelos com dados pré-processados
pipelines = []
pipelines.append(("ScaledLR", Pipeline([("Scaler", StandardScaler()), ("LR", LogisticRegression(solver="newton-cg"))])))
pipelines.append(("ScaledKNN", Pipeline([("Scaler", StandardScaler()),("KNN", KNeighborsClassifier())])))
pipelines.append(("ScaledCART", Pipeline([("Scaler", StandardScaler()),("CART", DecisionTreeClassifier())])))
pipelines.append(("ScaledNB", Pipeline([("Scaler", StandardScaler()),("NB",GaussianNB())])))
pipelines.append(("ScaledSVM", Pipeline([("Scaler", StandardScaler()),("SVM", SVC())])))

# Avaliando o modelo KNN com diferentes valores de hiperparâmetros
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_test)
k = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
distancias = ["euclidean", "manhattan", "minkowski"]
param_grid = dict(n_neighbors=k, metric=distancias)
model = KNeighborsClassifier()
kfold = KFold(n_splits=num_folds)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
grid_result = grid.fit(rescaledX, Y_train)
print("Melhor: %f usando %s" %(grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_["mean_test_score"]
stds = grid_result.cv_results_["std_test_score"]
params = grid_result.cv_results_["params"]
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f): %r" % (mean, stdev, param))

# Avaliando o modelo SVM com diferentes valores de hiperparâmetros
c_values = [0.1, 0.5, 1.0, 1.5, 2.0]
kernel_values = ["linear", "poly", "rbf", "sigmoid"]
param_grid = dict(C=c_values, kernel=kernel_values)
model = SVC()
kfold = KFold(n_splits=num_folds)
grid_result = grid.fit(rescaledX, Y_train)
means = grid_result.cv_results_["mean_test_score"]
stds = grid_result.cv_results_["std_test_score"]
params = grid_result.cv_results_["params"]
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f): %r" % (mean, stdev, param))

# Treinando um modelo de regressão logística e fazendo previsões no conjunto de teste
model = LogisticRegression(solver="newton-cg")
model.fit(X_train, Y_test)
predictions = model.predict(X_test)
print("Accuracy score = ", accuracy_score(Y_test, predictions))

# Criando e exibindo uma matriz de confusão
cm = confusion_matrix(Y_test, predictions)
labels = ["Sem diabetes", "Com diabetes"]
cmd = ConfusionMatrixDisplay(cm, display_labels=labels)
cmd.plot(values_format="d")
plt.show()

# Exibindo um relatório de classificação
print(classification_report(Y_test, predictions, target_names=labels))