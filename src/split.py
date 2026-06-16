

def split_temporal(df, data_corte='2017-01-01'):
    """
    Divide respeitando a ordem cronológica.
    Treino: antes do corte | Teste: a partir do corte.
    """
    train = df[df['date'] < data_corte].copy()
    test  = df[df['date'] >= data_corte].copy()

    pct_treino = len(train) / len(df) * 100
    print(f"Split temporal em '{data_corte}'")
    print(f"Treino: {len(train):,} amostras ({pct_treino:.1f}%)")
    print(f"Teste:  {len(test):,} amostras ({100 - pct_treino:.1f}%)")
    print(f"Período treino: {train['date'].min().date()} → {train['date'].max().date()}")
    print(f"Período teste:  {test['date'].min().date()} → {test['date'].max().date()}")

    return train, test
