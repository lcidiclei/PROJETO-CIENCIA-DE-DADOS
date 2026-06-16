# Previsão de Demanda e Reposição de Estoque com Machine Learning

**Projeto Final — Disciplina de Ciência de Dados**

## Problema e Objetivo

Prever a demanda futura de produtos utilizando histórico de vendas e gerar sugestões automáticas de reposição de estoque.

O objetivo é reduzir:

- Ruptura de estoque
- Excesso de produtos armazenados
- Custos operacionais
- Erros de planejamento

A previsão é realizada utilizando modelos de regressão supervisionada.

**Métrica primária:** SMAPE (Symmetric Mean Absolute Percentage Error), por ser adequada para problemas de previsão de demanda.

---

## Dataset

**Demand Forecasting Dataset (Kaggle)**

- 913.000 registros
- 10 lojas
- 50 produtos
- Período: 2013–2017

### Variáveis

| Variável | Descrição |
|-----------|------------|
| date | Data da venda |
| store | Identificador da loja |
| item | Identificador do produto |
| sales | Quantidade vendida |

### Download

O notebook realiza o download automaticamente do Kaggle quando as credenciais estiverem configuradas.

---

## Engenharia de Features

Foram criadas variáveis temporais e estatísticas para capturar sazonalidade e comportamento histórico das vendas.

### Features Temporais

- day
- month
- year
- dayofweek
- weekofyear
- quarter
- is_weekend

### Features de Histórico

- lag_1
- lag_7
- lag_30

### Features Estatísticas

- rolling_mean_7
- rolling_mean_30
- rolling_std_7

### Tendência

- trend

---

## Modelos Avaliados

### Linear Regression

Modelo baseline utilizado como referência para comparação.

### Random Forest Regressor

Parâmetros:

```python
n_estimators=200
max_depth=10
min_samples_leaf=5
random_state=42
```

### Gradient Boosting Regressor

Parâmetros:

```python
n_estimators=200
learning_rate=0.05
max_depth=5
random_state=42
```

---

## Métricas Utilizadas

### MAE

Mean Absolute Error (Erro Absoluto Médio).

### RMSE

Root Mean Squared Error (Raiz do Erro Quadrático Médio).

### SMAPE

Symmetric Mean Absolute Percentage Error.

### R²

Coeficiente de Determinação.

---

## Resultados

Substitua os valores abaixo pelos resultados obtidos em sua execução.

| Modelo | MAE | RMSE | SMAPE (%) | R² |
|----------|----------|----------|----------|----------|
| Linear Regression | XX.XX | XX.XX | XX.XX | X.XXXX |
| Random Forest | XX.XX | XX.XX | XX.XX | X.XXXX |
| Gradient Boosting | XX.XX | XX.XX | XX.XX | X.XXXX |

**Melhor modelo:** preencher após execução do notebook.

---

## Validação Estatística

Foi utilizado o **Teste de Wilcoxon** para verificar se a diferença entre os dois melhores modelos era estatisticamente significativa.

### Hipóteses

- H₀: Não existe diferença significativa entre os modelos.
- H₁: Existe diferença significativa entre os modelos.

### Nível de Significância

```text
α = 0.05
```

Interpretação:

- p-value < 0.05 → diferença significativa.
- p-value ≥ 0.05 → diferença não significativa.

---

## Visualizações Geradas

O pipeline produz automaticamente os seguintes gráficos:

### 1. Real vs Previsto

Comparação entre valores reais e previstos.

### 2. Comparação de Modelos

Comparação do SMAPE obtido pelos modelos.

### 3. Distribuição dos Resíduos

Análise dos erros do modelo.

### 4. Scatter Plot

Relação entre valores reais e previstos.

---

## Instalação e Execução

### Opção 1 — Docker

Construir a imagem:

```bash
docker build -t previsao-estoque .
```

Executar o container:

```bash
docker run -p 8888:8888 previsao-estoque
```

Acesse:

```text
http://localhost:8888
```

---

### Opção 2 — Google Colab

1. Abrir o notebook no Google Colab.
2. Executar todas as células em ordem.

---

### Opção 3 — Ambiente Local

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar o notebook:

```bash
jupyter notebook
```

---

## Estrutura do Repositório

```text
PROJETO-CIENCIA-DE-DADOS/
│
├── README.md
├── requirements.txt
├── Dockerfile
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── ciencia_de_dados.ipynb
│
├── src/
│   ├── forecasting.py
│   ├── pipeline.py
│   ├── loader.py
│   ├── features.py
│   ├── train.py
│   ├── evaluation.py
│   ├── statistics.py
│   ├── visualization.py
│   └── __init__.py
│
├── models/
│   └── modelo.pkl
│
├── article/
│   ├── artigo.md
│   ├── referencias.bib
│   ├── figures/
│   └── tables/
│
└── docs/
    ├── decisoes-tecnicas.md
    └── dicionario-de-dados.md
```

---

## Reprodutibilidade

Todos os modelos utilizam:

```python
random_state=42
```

As métricas e parâmetros são registrados automaticamente utilizando **MLflow**.

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- SciPy
- MLflow
- Joblib
- Docker

---

## Limitações

- Não foi realizada busca exaustiva de hiperparâmetros.
- O modelo utiliza apenas histórico de vendas.
- Não considera fatores externos como clima, promoções ou feriados.
- Resultados dependem da qualidade dos dados históricos.

Consulte `docs/decisoes tecnicas.md` para justificativas completas e `article/artigo.md` para a análise acadêmica detalhada.
