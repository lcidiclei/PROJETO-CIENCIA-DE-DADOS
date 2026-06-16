from scipy.stats import wilcoxon
import numpy as np
import pandas as pd

def comparar_modelos(resultados, y_test):
    df_metricas = pd.DataFrame([
        {
            "Modelo": nome,
            "RMSE": dados["RMSE"]
        }
        for nome, dados in resultados.items()
    ]).sort_values("RMSE")

    modelo_1 = df_metricas.iloc[0]["Modelo"]
    modelo_2 = df_metricas.iloc[1]["Modelo"]

    print(f"Comparando modelos: {modelo_1} vs {modelo_2}")

    erro_1 = np.abs(
        y_test.values - resultados[modelo_1]["pred"]
    )

    erro_2 = np.abs(
        y_test.values - resultados[modelo_2]["pred"]
    )

    stat, p_value = wilcoxon(
        erro_1,
        erro_2
    )

    print(f"Estatística de Wilcoxon: {stat:.4f}")
    print(f"p-value: {p_value:.6f}")

    if p_value < 0.05:
        print(
            "Diferença estatisticamente significativa entre os modelos."
        )
    else:
        print(
            "Não foi encontrada diferença estatisticamente significativa."
        )

    return stat, p_value
