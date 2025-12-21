# 🚢 Classificação Binária - Titanic Dataset

Projeto de Machine Learning para prever a sobrevivência de passageiros do Titanic utilizando Regressão Logística.

## 📋 Descrição

Este projeto implementa um modelo de classificação binária que prediz se um passageiro do Titanic sobreviveu ou não ao naufrágio, baseado em características como idade, sexo, classe do ticket, número de familiares a bordo, entre outros.

O modelo utiliza **Regressão Logística** e alcança uma precisão de aproximadamente **83.71%** nos dados de teste.

## 🎯 Objetivo

Classificar os passageiros do Titanic em duas categorias:
- **0**: Não sobreviveu
- **1**: Sobreviveu

## 📊 Dataset

O dataset utilizado é o famoso **Titanic Dataset**, que contém informações sobre 891 passageiros. As features utilizadas incluem:

- **Pclass**: Classe do ticket (1ª, 2ª ou 3ª classe)
- **Sex**: Sexo do passageiro
- **Age**: Idade do passageiro
- **SibSp**: Número de irmãos/cônjuges a bordo
- **Parch**: Número de pais/filhos a bordo
- **Fare**: Tarifa paga pelo ticket
- **Embarked**: Porto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton)

### Tratamento dos Dados

O projeto realiza as seguintes etapas de pré-processamento:

1. **Remoção de colunas irrelevantes**: Name, Ticket, Cabin, PassengerId
2. **Tratamento de valores faltantes**: 
   - Idade preenchida com a mediana
   - Remoção de linhas com embarque faltante
3. **Codificação de variáveis categóricas**: Conversão de Sex e Embarked em variáveis binárias (One-Hot Encoding)
4. **Normalização**: Escalonamento dos dados usando StandardScaler (média 0, desvio padrão 1)

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **pandas**: Manipulação de dados
- **numpy**: Operações numéricas
- **scikit-learn**: Algoritmos de Machine Learning
- **matplotlib**: Visualização de dados
- **seaborn**: Visualização estatística
- **Jupyter Notebook**: Ambiente interativo (opcional)

## 📦 Instalação

### Pré-requisitos

- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/titanic-classification.git
cd titanic-classification
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**

- **Windows:**
```bash
venv\Scripts\activate
```

- **Linux/Mac:**
```bash
source venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

## 🚀 Como Executar

### Opção 1: Executar o script Python

```bash
python ClassificBinaria.py
```

Este script irá:
- Carregar o dataset
- Realizar o pré-processamento
- Treinar o modelo
- Exibir a precisão alcançada

### Opção 2: Executar o Jupyter Notebook

```bash
jupyter notebook classific.ipynb
```

O notebook contém:
- Análise exploratória dos dados
- Visualizações detalhadas
- Matriz de confusão
- Métricas de avaliação

## 📈 Resultados

O modelo alcança os seguintes resultados:

- **Precisão (Accuracy)**: ~83.71%
- **Matriz de Confusão**:
  - 90 mortos classificados corretamente
  - 59 sobreviventes classificados corretamente
  - 15 falsos negativos (sobreviventes classificados como mortos)
  - 14 falsos positivos (mortos classificados como sobreviventes)

## 📁 Estrutura do Projeto

```
titanic-classification/
│
├── ClassificBinaria.py      # Script principal
├── classific.ipynb           # Notebook com análise detalhada
├── Titanic-Dataset.csv       # Dataset do Titanic
├── .gitignore                # Arquivos ignorados pelo Git
├── README.md                 # Este arquivo
└── venv/                     # Ambiente virtual (não versionado)
```

## 🔍 Detalhes Técnicos

### Divisão dos Dados

- **Treinamento**: 80% dos dados (711 amostras)
- **Teste**: 20% dos dados (178 amostras)

### Parâmetros do Modelo

O modelo utiliza Regressão Logística com parâmetros padrão do scikit-learn:
- Solver: lbfgs
- Max iterations: 100
- Regularização: L2

### Escalonamento

Os dados são normalizados usando `StandardScaler`, garantindo que todas as features tenham:
- Média = 0
- Desvio padrão = 1

Isso evita que features com valores maiores (como Fare) dominem o treinamento.

## 🎓 Conceitos de Machine Learning

Este projeto é ideal para aprender sobre:

- **Classificação Binária**: Prever uma de duas classes possíveis
- **Regressão Logística**: Algoritmo linear para classificação
- **Pré-processamento de Dados**: Limpeza e preparação de dados reais
- **Validação de Modelos**: Divisão treino/teste e métricas de avaliação
- **Normalização**: Importância do escalonamento de features

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abrir um Pull Request

## 📝 Melhorias Futuras

- [ ] Implementar outros algoritmos (Random Forest, SVM, XGBoost)
- [ ] Realizar feature engineering (criar novas features)
- [ ] Implementar validação cruzada
- [ ] Adicionar hyperparameter tuning
- [ ] Criar uma interface web para predições
- [ ] Adicionar análise de feature importance

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

## 📞 Contato

- GitHub: Pedroct06
- LinkedIn: Em breve
- Email: pedrocoelhotorres@outlook.com

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!