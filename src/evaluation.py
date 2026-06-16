from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def smape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    denominador = (np.abs(y_true) + np.abs(y_pred)) / 2
    mask = denominador != 0
    return np.mean(np.abs(y_true[mask] - y_pred[mask]) / denominador[mask]) * 100

mlflow.set_experiment("Previsao_Estoque")
