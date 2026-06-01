# PROJETO CIÊNCIA DE DADOS

## Previsão Inteligente de Reabastecimento de Estoque com Base no Histórico de Compras

### Integrantes

* Iago Baldini dos Santos
* Lucas Uriel Diniz Queiroz
* Alexandre Luis Teixeira Santos
* Lucas Cidiclei Pereira da Silva

## Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de Ciência de Dados Aplicada com o objetivo de prever a demanda futura de produtos utilizando dados históricos de vendas.

A proposta é utilizar técnicas de Machine Learning para auxiliar empresas no planejamento de estoque, reduzindo tanto a falta de produtos quanto o excesso de mercadorias armazenadas.

## Problema

Muitas empresas enfrentam dificuldades para decidir quando e quanto reabastecer seus estoques. Quando essa decisão é tomada apenas com base na experiência ou observação manual, podem ocorrer problemas como:

* Falta de produtos para venda;
* Excesso de estoque;
* Aumento dos custos de armazenamento;
* Perda de vendas e de clientes.

Com isso, buscamos criar um modelo capaz de analisar o histórico de vendas e gerar previsões que auxiliem esse processo de tomada de decisão.

## Base de Dados

Foi utilizado um conjunto de dados de previsão de demanda disponível no Kaggle, contendo informações sobre:

* Data da venda;
* Loja;
* Produto;
* Quantidade vendida.

## Etapas do Projeto

### 1. Carregamento dos Dados

Inicialmente os dados são carregados e verificados para garantir que a leitura foi realizada corretamente.

### 2. Análise Exploratória

Foram realizadas análises para entender a estrutura do conjunto de dados, verificar possíveis valores ausentes e observar o comportamento das vendas ao longo do tempo.

### 3. Engenharia de Atributos

Foram criadas novas variáveis para auxiliar os modelos na identificação de padrões temporais:

* Dia
* Mês
* Dia da semana
* Semana do ano
* Lag de 1 dia
* Lag de 7 dias
* Média móvel de 7 dias

### 4. Divisão Temporal

Os dados foram separados em treino e teste respeitando a ordem cronológica dos registros, evitando vazamento de informações futuras para o modelo.

### 5. Treinamento dos Modelos

Modelos utilizados:

* Linear Regression
* Random Forest Regressor

### 6. Avaliação

O desempenho dos modelos foi avaliado utilizando a métrica RMSE (Root Mean Squared Error).

## Estrutura do Repositório

```text
data/
notebooks/
src/
models/
reports/
```

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Git
* GitHub
* Docker

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/lcidiclei/PROJETO-CIENCIA-DE-DADOS.git
```

Entre na pasta:

```bash
cd PROJETO-CIENCIA-DE-DADOS
```

Execute o projeto:

```bash
python src/pipeline.py
```

## Observação

Este projeto possui finalidade exclusivamente acadêmica e foi desenvolvido como parte da avaliação da disciplina de Ciência de Dados Aplicada.
