# Dicionário de Dados

## Dataset

Store Item Demand Forecasting Challenge

---

## Variáveis Originais

| Variável | Tipo     | Descrição                       |
| -------- | -------- | ------------------------------- |
| date     | datetime | Data da venda                   |
| store    | inteiro  | Identificador da loja           |
| item     | inteiro  | Identificador do produto        |
| sales    | inteiro  | Quantidade de unidades vendidas |

---

## Variável Alvo

| Variável | Tipo    | Descrição                                                 |
| -------- | ------- | --------------------------------------------------------- |
| sales    | inteiro | Quantidade vendida utilizada para treinamento dos modelos |

---

## Variáveis Criadas (Feature Engineering)

### day

Dia do mês.

| Tipo    |
| ------- |
| inteiro |

---

### month

Mês da venda.

| Tipo    |
| ------- |
| inteiro |

---

### year

Ano da venda.

| Tipo    |
| ------- |
| inteiro |

---

### dayofweek

Dia da semana.

Valores:

| Valor | Significado   |
| ----- | ------------- |
| 0     | Segunda-feira |
| 1     | Terça-feira   |
| 2     | Quarta-feira  |
| 3     | Quinta-feira  |
| 4     | Sexta-feira   |
| 5     | Sábado        |
| 6     | Domingo       |

---

### weekofyear

Semana do ano.

| Tipo    |
| ------- |
| inteiro |

---

### quarter

Trimestre do ano.

Valores possíveis:

```text
1, 2, 3, 4
```

---

### is_weekend

Indica se a data pertence ao final de semana.

| Valor | Significado |
| ----- | ----------- |
| 0     | Não         |
| 1     | Sim         |

---

### lag_1

Quantidade vendida no dia anterior.

| Tipo     |
| -------- |
| numérico |

---

### lag_7

Quantidade vendida sete dias antes.

| Tipo     |
| -------- |
| numérico |

---

### lag_30

Quantidade vendida trinta dias antes.

| Tipo     |
| -------- |
| numérico |

---

### rolling_mean_7

Média móvel dos últimos sete dias.

| Tipo     |
| -------- |
| numérico |

---

### rolling_mean_30

Média móvel dos últimos trinta dias.

| Tipo     |
| -------- |
| numérico |

---

### rolling_std_7

Desvio padrão móvel dos últimos sete dias.

| Tipo     |
| -------- |
| numérico |

---

### trend

Variável sequencial utilizada para capturar tendência temporal.

| Tipo    |
| ------- |
| inteiro |

---

## Variáveis Utilizadas no Treinamento

```python
FEATURES = [
    'day',
    'month',
    'year',
    'dayofweek',
    'weekofyear',
    'is_weekend',
    'quarter',
    'lag_1',
    'lag_7',
    'lag_30',
    'rolling_mean_7',
    'rolling_mean_30',
    'rolling_std_7',
    'trend'
]
```

---

## Variável Predita

```text
sales
```

Representa a previsão de demanda diária utilizada para gerar recomendações automáticas de reabastecimento de estoque.
