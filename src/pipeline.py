from features import carregar_dataset, criar_features
from split import split_temporal
from train import treinar_modelos
from evaluate import plot_previsao


def pipeline_completo(df):

    df = criar_features(df)

    train, test = split_temporal(df)

    features = [
        'day',
        'month',
        'dayofweek',
        'weekofyear',
        'lag_1',
        'lag_7',
        'rolling_mean_7'
    ]

    X_train = train[features]
    y_train = train['sales']

    X_test = test[features]
    y_test = test['sales']

    resultados = treinar_modelos(
        X_train,
        y_train,
        X_test,
        y_test
    )

    melhor = min(
        resultados.items(),
        key=lambda x: x[1]['RMSE']
    )

    return melhor[1]['modelo'], X_test, y_test


if __name__ == "__main__":

    df = carregar_dataset("train.csv")

    modelo, X_test, y_test = pipeline_completo(df)

    pred = modelo.predict(X_test)

    plot_previsao(y_test, pred)