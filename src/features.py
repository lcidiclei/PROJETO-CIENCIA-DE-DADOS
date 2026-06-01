import pandas as pd

def carregar_dataset(caminho):
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for enc in encodings:
        try:
            df = pd.read_csv(caminho, encoding=enc)
            print(f"Carregado com encoding: {enc}")
            return df
        except:
            print(f"Falhou com {enc}")

    return None


def criar_features(df):
    df = df.copy()

    df['date'] = pd.to_datetime(df['date'])

    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['dayofweek'] = df['date'].dt.dayofweek
    df['weekofyear'] = df['date'].dt.isocalendar().week.astype(int)

    df = df.sort_values(['store','item','date'])

    df['lag_1'] = df.groupby(['store','item'])['sales'].shift(1)
    df['lag_7'] = df.groupby(['store','item'])['sales'].shift(7)

    df['rolling_mean_7'] = (
        df.groupby(['store','item'])['sales']
        .shift(1)
        .rolling(7)
        .mean()
    )

    df = df.dropna()

    return df