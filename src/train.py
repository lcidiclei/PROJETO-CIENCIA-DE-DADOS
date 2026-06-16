import mlflow
import mlflow.sklearn
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from src.evaluate import smape

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

    print(f"{'Modelo':<20} {'MAE':>10} {'RMSE':>10} {'SMAPE':>10}")
    print("-" * 60)

    for nome, modelo in modelos.items():

        with mlflow.start_run(run_name=nome):

            modelo.fit(X_train, y_train)

            pred = modelo.predict(X_test)
            pred = np.clip(pred, 0, None)

            mae_val = mean_absolute_error(y_test, pred)
            rmse_val = np.sqrt(mean_squared_error(y_test, pred))
            smape_val = smape(y_test, pred)
            r2_val = r2_score(y_test, pred)

            mlflow.log_param("modelo", nome)

            if hasattr(modelo, "n_estimators"):
                mlflow.log_param("n_estimators", modelo.n_estimators)

            mlflow.log_metric("MAE", mae_val)
            mlflow.log_metric("RMSE", rmse_val)
            mlflow.log_metric("SMAPE", smape_val)
            mlflow.log_metric("R2", r2_val)

            mlflow.sklearn.log_model(modelo, "modelo")

            resultados[nome] = {
                "modelo": modelo,
                "pred": pred,
                "MAE": mae_val,
                "RMSE": rmse_val,
                "SMAPE": smape_val,
                "R2": r2_val
            }

            print(
                f"{nome:<20} "
                f"{mae_val:>10.2f} "
                f"{rmse_val:>10.2f} "
                f"{smape_val:>9.2f}%"
                f"{r2_val:>9.4f}"
            )

    print("\nResumo dos Modelos")

    df_metricas = pd.DataFrame([
          {
              "Modelo": nome,
              "MAE": round(dados["MAE"], 2),
              "RMSE": round(dados["RMSE"], 2),
              "SMAPE (%)": round(dados["SMAPE"], 2),
              "R²": round(dados["R2"], 4)
          }
          for nome, dados in resultados.items()
      ]).sort_values(by="RMSE")

    display(df_metricas)

    melhor_modelo = df_metricas.iloc[0]["Modelo"]

    print(f"\nMelhor modelo selecionado: {melhor_modelo}")


    return resultados
