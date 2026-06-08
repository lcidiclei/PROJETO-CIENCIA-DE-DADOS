from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

import numpy as np
import mlflow
import mlflow.sklearn


def smape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)

    denominador = (np.abs(y_true) + np.abs(y_pred)) / 2

    mask = denominador != 0

    return np.mean(
        np.abs(y_true[mask] - y_pred[mask]) / denominador[mask]
    ) * 100


mlflow.set_experiment("Previsao_Estoque")


def treinar_modelos(X_train, y_train, X_test, y_test):

    modelos = {
        "LinearRegression": LinearRegression(),

        "RandomForest": RandomForestRegressor(
            n_estimators=200,
            max_depth=10,
            min_samples_leaf=5,
            n_jobs=-1,
            random_state=42
        ),

        "GradientBoosting": GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=5,
            random_state=42
        )
    }

    resultados = {}

    for nome, modelo in modelos.items():

        with mlflow.start_run(run_name=nome):

            modelo.fit(X_train, y_train)

            pred = modelo.predict(X_test)
            pred = np.clip(pred, 0, None)

            mae_val = mean_absolute_error(y_test, pred)
            rmse_val = np.sqrt(mean_squared_error(y_test, pred))
            smape_val = smape(y_test, pred)

            mlflow.log_param("modelo", nome)
            mlflow.log_metric("MAE", mae_val)
            mlflow.log_metric("RMSE", rmse_val)
            mlflow.log_metric("SMAPE", smape_val)

            mlflow.sklearn.log_model(
                modelo,
                artifact_path=nome
            )

            resultados[nome] = {
                "modelo": modelo,
                "pred": pred,
                "MAE": mae_val,
                "RMSE": rmse_val,
                "SMAPE": smape_val
            }

            print(
                f"{nome} | MAE={mae_val:.2f} | "
                f"RMSE={rmse_val:.2f} | "
                f"SMAPE={smape_val:.2f}%"
            )

    return resultados
