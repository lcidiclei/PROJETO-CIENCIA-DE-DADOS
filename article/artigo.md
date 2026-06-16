\# Previsão Inteligente de Reabastecimento de Estoque com Base no Histórico de Compras Utilizando Machine Learning



\*\*Disciplina:\*\* Machine Learning – AV2



\## Resumo



A previsão de demanda é uma atividade essencial para o gerenciamento eficiente de estoques, permitindo reduzir custos operacionais e minimizar perdas decorrentes de excesso ou falta de produtos. Este trabalho apresenta uma solução baseada em aprendizado de máquina para previsão de demanda utilizando o dataset Store Item Demand Forecasting Challenge. Foram avaliados três algoritmos de regressão: Linear Regression, Random Forest Regressor e Gradient Boosting Regressor. O processo incluiu análise exploratória dos dados, engenharia de atributos temporais, criação de variáveis de defasagem, médias móveis, treinamento supervisionado, rastreamento de experimentos com MLflow e disponibilização do modelo através de FastAPI e Docker. Os modelos foram avaliados utilizando as métricas MAE, RMSE, SMAPE e R². Os resultados demonstraram que modelos baseados em ensembles apresentaram melhor desempenho para o problema estudado, permitindo gerar previsões de vendas e recomendações automáticas de reabastecimento.



\*\*Palavras-chave:\*\* previsão de demanda, machine learning, estoque, Random Forest, Gradient Boosting, MLflow.



\# 1. Introdução



A gestão de estoques é um dos principais desafios enfrentados por empresas do setor varejista. Decisões inadequadas de reabastecimento podem gerar perdas financeiras devido à indisponibilidade de produtos ou ao excesso de itens armazenados.



Com o avanço das técnicas de aprendizado de máquina, tornou-se possível utilizar dados históricos para prever demandas futuras com maior precisão. Este trabalho propõe a construção de um sistema inteligente de previsão de demanda capaz de auxiliar processos de reabastecimento utilizando algoritmos supervisionados de regressão.



\# 2. Revisão de Literatura



A previsão de demanda é amplamente utilizada em cadeias de suprimentos para melhorar a eficiência operacional e reduzir custos. Métodos estatísticos tradicionais, embora úteis, possuem limitações para capturar padrões complexos presentes em grandes volumes de dados.



Modelos de ensemble, como Random Forest e Gradient Boosting, apresentam capacidade superior para modelar relações não lineares e identificar interações entre variáveis. Estudos recentes demonstram que essas técnicas frequentemente superam modelos lineares em tarefas de previsão de demanda.



\# 3. Metodologia



\## 3.1 Dataset



Foi utilizado o dataset Store Item Demand Forecasting Challenge disponibilizado pela plataforma Kaggle.



As variáveis originais são:



\* date

\* store

\* item

\* sales



A variável alvo utilizada foi:



\* sales



\## 3.2 Análise Exploratória



Foram realizadas análises para identificar:



\* Distribuição das vendas;

\* Comportamento temporal;

\* Tendências anuais;

\* Padrões por loja;

\* Padrões por produto.



\## 3.3 Engenharia de Atributos



Foram criadas variáveis temporais:



\* day

\* month

\* year

\* dayofweek

\* weekofyear

\* quarter

\* is\_weekend



Variáveis históricas:



\* lag\_1

\* lag\_7

\* lag\_30



Estatísticas móveis:



\* rolling\_mean\_7

\* rolling\_mean\_30

\* rolling\_std\_7



Além disso, foi criada uma variável de tendência denominada trend.



\## 3.4 Divisão Temporal



A separação dos dados respeitou a ordem cronológica.



Treinamento:



\* Dados anteriores a 01/01/2017.



Teste:



\* Dados posteriores a 01/01/2017.



\## 3.5 Modelos Avaliados



\* Linear Regression

\* Random Forest Regressor

\* Gradient Boosting Regressor



\## 3.6 Métricas



Foram utilizadas as seguintes métricas:



\* Mean Absolute Error (MAE)

\* Root Mean Squared Error (RMSE)

\* Symmetric Mean Absolute Percentage Error (SMAPE)

\* Coeficiente de Determinação (R²)



Também foi aplicado o teste estatístico de Wilcoxon para comparação dos dois melhores modelos.



\# 4. Resultados



Os modelos foram treinados utilizando as mesmas variáveis e comparados através das métricas definidas.



Foram geradas visualizações de:



\* Real versus Previsto;

\* Comparação entre modelos;

\* Distribuição dos resíduos;

\* Scatter Plot entre valores reais e previstos.



O modelo com menor erro e melhor capacidade explicativa foi selecionado para gerar previsões futuras e recomendações de reabastecimento.



\# 5. Discussão



Os resultados demonstram que a utilização de variáveis históricas e estatísticas móveis melhora significativamente a qualidade das previsões.



Modelos baseados em árvores apresentaram melhor desempenho quando comparados à Regressão Linear, indicando a presença de relações não lineares nos dados.



O uso de MLflow permitiu rastrear experimentos e comparar modelos de forma organizada, enquanto FastAPI e Docker facilitaram a disponibilização da solução.



\# 6. Limitações



Entre as limitações observadas destacam-se:



\* Ausência de variáveis externas como promoções e feriados;

\* Dependência exclusiva do histórico de vendas;

\* Dataset representando apenas um cenário específico de varejo.



\# 7. Conclusão



Este trabalho apresentou uma solução completa para previsão inteligente de demanda utilizando técnicas de aprendizado de máquina.



Os resultados demonstraram que modelos ensemble apresentam desempenho superior para o problema estudado, permitindo gerar previsões confiáveis e auxiliar decisões de reabastecimento de estoque.



Como trabalhos futuros recomenda-se explorar modelos especializados para séries temporais, como XGBoost, LightGBM, Prophet e redes neurais recorrentes.



