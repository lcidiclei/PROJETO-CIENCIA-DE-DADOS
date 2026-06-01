# PROJETO-CIENCIA-DE-DADOS
# Previsão Inteligente de Reabastecimento de Estoque com Base no Histórico de Compras

- Integrantes

* Iago Baldini dos Santos
* Lucas Uriel Diniz
* Alexandre Luis Teixeira
* Lucas Cidiclei Pereira

- Sobre o projeto

Este projeto foi desenvolvido para a disciplina de Ciência de Dados Aplicada com o objetivo de prever a demanda futura de produtos utilizando dados históricos de vendas.

A ideia é usar técnicas de Machine Learning para auxiliar empresas no planejamento de estoque, ajudando a reduzir tanto a falta de produtos quanto o excesso de mercadorias armazenadas.

- Problema

Muitas empresas enfrentam dificuldades para decidir quando e quanto reabastecer seus estoques. Quando essa decisão é tomada apenas com base na experiência ou observação manual, podem ocorrer problemas como:

* Falta de produtos para venda;
* Excesso de estoque;
* Aumento dos custos de armazenamento;
* Perda de vendas e de clientes.

Com isso, buscamos criar um modelo capaz de analisar o histórico de vendas e gerar previsões que possam apoiar esse processo de tomada de decisão.

- Base de Dados

Foi utilizado um conjunto de dados de previsão de demanda disponível no Kaggle, contendo informações sobre:

* Data da venda;
* Loja;
* Produto;
* Quantidade vendida.

- Etapas do Projeto

1. Carregamento dos dados

Inicialmente os dados são carregados e verificados para garantir que a leitura foi realizada corretamente.

2. Análise exploratória

Foram realizadas análises para entender a estrutura do conjunto de dados, verificar possíveis valores ausentes e observar o comportamento das vendas ao longo do tempo.

3. Engenharia de atributos

Foram criadas novas variáveis para auxiliar os modelos na identificação de padrões temporais, incluindo:

* Dia;
* Mês;
* Dia da semana;
* Semana do ano;
* Lag de 1 dia;
* Lag de 7 dias;
* Média móvel de 7 dias.

4. Divisão temporal

Os dados foram separados em treino e teste respeitando a ordem cronológica dos registros, evitando vazamento de informações futuras para o modelo.

5. Treinamento dos modelos

Foram utilizados os seguintes algoritmos:

* Linear Regression
* Random Forest Regressor

6. Avaliação

O desempenho dos modelos foi avaliado utilizando a métrica RMSE (Root Mean Squared Error), permitindo comparar a qualidade das previsões realizadas.

- Estrutura do Repositório


data/
notebooks/
src/
models/
reports/


- Tecnologias utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Git
* GitHub
* Docker

- Como executar

Clone o repositório:


git clone URL_DO_REPOSITORIO


Entre na pasta:


cd PROJETO-CIENCIA-DE-DADOS


Execute o projeto:


python src/pipeline.py


- Observação

Este projeto possui finalidade exclusivamente acadêmica e foi desenvolvido como parte da avaliação da disciplina de Ciência de Dados Aplicada.

