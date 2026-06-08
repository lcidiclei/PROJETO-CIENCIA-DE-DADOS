from features import carregar_dataset, criar_features
from split import split_temporal
from train import treinar_modelos
from evaluate import plot_resultados


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


def pipeline_completo(df):

    df_feat = criar_features(df)

    train, test = split_temporal(df_feat)

    X_train = train[FEATURES]
    y_train = train['sales']

    X_test = test[FEATURES]
    y_test = test['sales']

    resultados = treinar_modelos(
        X_train,
        y_train,
        X_test,
        y_test
    )

    melhor_nome, melhor = min(
        resultados.items(),
        key=lambda x: x[1]['SMAPE']
    )

    print(
        f"Melhor modelo: "
        f"{melhor_nome} "
        f"(SMAPE={melhor['SMAPE']:.2f}%)"
    )

    return (
        melhor['modelo'],
        melhor['pred'],
        X_test,
        y_test
    )


if __name__ == "__main__":

    df = carregar_dataset("data/train.csv")

    modelo, pred, X_test, y_test = pipeline_completo(df)

    plot_resultados(y_test, pred)
