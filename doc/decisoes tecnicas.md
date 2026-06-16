# Decisões Técnicas do Projeto

## 1. Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema inteligente de previsão de demanda para auxiliar processos de reabastecimento de estoque utilizando técnicas de Machine Learning.

A solução foi construída utilizando dados históricos de vendas do dataset Store Item Demand Forecasting Challenge, disponibilizado pela plataforma Kaggle.

---

## 2. Escolha do Dataset

Foi utilizado o dataset Store Item Demand Forecasting Challenge por apresentar características adequadas para problemas de previsão de demanda.

O conjunto de dados contém:

* Histórico diário de vendas;
* Múltiplas lojas;
* Múltiplos produtos;
* Série temporal de longo prazo.

Essas características permitem simular cenários reais de gestão de estoque.

---

## 3. Variável Alvo

A variável alvo definida para o treinamento dos modelos foi:

```text
sales
```

Essa variável representa a quantidade de unidades vendidas em determinado dia para um produto específico em uma determinada loja.

---

## 4. Estratégia de Divisão dos Dados

Foi utilizada divisão temporal em vez de divisão aleatória.

Treinamento:

```text
Dados anteriores a 01/01/2017
```

Teste:

```text
Dados posteriores a 01/01/2017
```

Essa abordagem evita vazamento de informações futuras para o treinamento e reproduz melhor um cenário real de previsão.

---

## 5. Engenharia de Atributos

Foram criadas variáveis derivadas da data:

* day
* month
* year
* dayofweek
* weekofyear
* quarter
* is_weekend

Além disso, foram criadas variáveis históricas:

* lag_1
* lag_7
* lag_30

Também foram utilizadas estatísticas móveis:

* rolling_mean_7
* rolling_mean_30
* rolling_std_7

Foi criada ainda uma variável de tendência temporal denominada trend.

Essas variáveis foram escolhidas para capturar sazonalidade, comportamento histórico e tendências de vendas.

---

## 6. Modelos Avaliados

Foram avaliados três algoritmos:

### Linear Regression

Utilizado como modelo baseline devido à sua simplicidade e interpretabilidade.

### Random Forest Regressor

Escolhido por sua capacidade de modelar relações não lineares e reduzir overfitting através do uso de múltiplas árvores.

### Gradient Boosting Regressor

Selecionado por apresentar bom desempenho em problemas tabulares e capacidade de capturar padrões complexos.

---

## 7. Métricas Utilizadas

Foram utilizadas as seguintes métricas:

### MAE

Erro absoluto médio das previsões.

### RMSE

Raiz do erro quadrático médio.

Penaliza erros maiores com maior intensidade.

### SMAPE

Erro percentual absoluto médio simétrico.

Facilita a interpretação do desempenho em termos percentuais.

### R²

Coeficiente de determinação.

Indica a proporção da variabilidade dos dados explicada pelo modelo.

---

## 8. Seleção do Melhor Modelo

A seleção do melhor modelo foi realizada utilizando principalmente o RMSE e o SMAPE.

O modelo com menor erro foi escolhido para gerar previsões futuras e recomendações de reabastecimento.

---

## 9. Validação Estatística

Foi aplicado o teste de Wilcoxon para comparação dos dois melhores modelos.

O objetivo foi verificar se as diferenças observadas entre os erros eram estatisticamente significativas.

---

## 10. Rastreamento de Experimentos

Foi utilizado o MLflow para:

* Registro de parâmetros;
* Registro de métricas;
* Armazenamento de modelos;
* Comparação de experimentos.

---

## 11. Disponibilização da Solução

A solução foi disponibilizada através de:

### FastAPI

Responsável pela criação da API REST.

### Docker

Responsável pela padronização e reprodutibilidade do ambiente de execução.

---

## 12. Limitações

As previsões foram realizadas exclusivamente com base no histórico de vendas.

Não foram considerados fatores externos como:

* Promoções;
* Feriados;
* Condições climáticas;
* Eventos especiais.

Esses fatores podem ser explorados em trabalhos futuros.
