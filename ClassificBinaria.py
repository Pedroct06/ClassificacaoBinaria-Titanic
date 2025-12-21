import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Carrega o dataset, que falta eu pegar no kaggle
df = pd.read_csv("Titanic-Dataset.csv")

#Tratamento dos dados do dataSet. Dropei as colunas com o nome, o ticket, a cabine e o Id dos passageiros, para melhor otimização
#E porque não são tão relevantes, além disso preechi os valores faltantes na coluna de idade com a mediana dessa coluna, e dropei
# a coluna do local onde foram embarcados, além disso criei a coluna de família na tentativa de melhorar a precisão
#df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
#df["IsAlone"] = 1
#df.loc[df["FamilySize"] > 1, ["IsAlone"]] = 0
df = df.drop(["Name", "Ticket", "Cabin", "PassengerId"], axis=1)
df["Age"] = df["Age"].fillna(df["Age"].median())
df = df.dropna(subset = "Embarked")

#Define a coluna que eu quero classificar/prever
Coluna = "Survived"

#Pega todas as colunas, menos a coluna que eu escolhi
X = df.drop(Coluna, axis=1)

#Pega a coluna que eu escolhi
Y = df[Coluna]

#Transforma o texto em binário
X = pd.get_dummies(X, drop_first=True)

#Cria as variáveis que eu vou utilizar para treinar e testar, defini o padrão para 70% dos dados para treinto, e 30% para teste
X_treino, X_test, Y_treino, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

#Vou escalonar os dados para ficar na faixa entre 0 e 1, para não ter desregulação de pesos
scalonamento = StandardScaler()

#treinar o X, com o escalonamento, utilizando fit_transform para aprender a média e o desvio dos dados
X_treino = scalonamento.fit_transform(X_treino)

#Transformar o teste, usando a média e desvio que aprendeu no fit_transform, utilizamos apenas o transform e não o fit_transform
#pois queremos utilizar a mesma regua de média calcula com os dados de treino
X_test = scalonamento.transform(X_test)

#criando o modelo
modelo = LogisticRegression()
#Treinando o modelo utilizando os dados de teste de X, para prever o Y
modelo.fit(X_treino,Y_treino)

#Guardando em uma variável a precisão do modelo
precisao = modelo.score(X_test,Y_test)

#Imprimindo a precisao
print(F"Precisao igual a: {precisao * 100:.2f}%")

