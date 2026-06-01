from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np


def treinar_modelos(X_train, y_train, X_test, y_test):

    modelos = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(n_estimators=50)
    }

    resultados = {}

    for nome, modelo in modelos.items():

        modelo.fit(X_train, y_train)

        pred = modelo.predict(X_test)

        mae = mean_absolute_error(y_test, pred)
        rmse = np.sqrt(((y_test - pred) ** 2).mean())

        resultados[nome] = {
            "modelo": modelo,
            "RMSE": rmse
        }

        print(f"{nome} -> RMSE: {rmse:.2f}")

    return resultados