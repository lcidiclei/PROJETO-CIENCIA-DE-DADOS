from src.feature_engineering import criar_features
from src.preprocessing import split_temporal
from src.train import treinar_modelos

FEATURES = [
    'day', 'month', 'year', 'dayofweek', 'weekofyear',
    'is_weekend', 'quarter',
    'lag_1', 'lag_7', 'lag_30',
    'rolling_mean_7', 'rolling_mean_30', 'rolling_std_7',
    'trend'
]


def pipeline_completo(df, data_corte='2017-01-01'):
    print("\n" + "=" * 48)
    print("ETAPA 1 — Feature Engineering")
    print("=" * 48)
    df_feat = criar_features(df)

    print("\n" + "=" * 48)
    print("ETAPA 2 — Split Temporal")
    print("=" * 48)
    train, test = split_temporal(df_feat, data_corte)

    X_train = train[FEATURES]
    y_train = train['sales']
    X_test  = test[FEATURES]
    y_test  = test['sales']

    print("\n" + "=" * 48)
    print("ETAPA 3 — Treinamento")
    print("=" * 48)
    resultados = treinar_modelos(X_train, y_train, X_test, y_test)

    melhor_nome, melhor = min(resultados.items(), key=lambda x: x[1]['SMAPE'])
    print(f"\nMelhor modelo: {melhor_nome} (SMAPE={melhor['SMAPE']:.2f}%)")

    return melhor['modelo'], melhor['pred'], X_test, y_test, test, resultados
