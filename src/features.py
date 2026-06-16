import pandas as pd

def criar_features(df):
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])

    # --- Features temporais ---
    df['day']        = df['date'].dt.day
    df['month']      = df['date'].dt.month
    df['year']       = df['date'].dt.year
    df['dayofweek']  = df['date'].dt.dayofweek
    df['weekofyear'] = df['date'].dt.isocalendar().week.astype(int)
    df['is_weekend'] = (df['dayofweek'] >= 5).astype(int)
    df['quarter']    = df['date'].dt.quarter

    # --- Ordenação essencial para lags correrem por grupo ---
    df = df.sort_values(['store', 'item', 'date']).reset_index(drop=True)

    grupo = df.groupby(['store', 'item'])['sales']

    # --- Lags ---
    df['lag_1']  = grupo.shift(1)
    df['lag_7']  = grupo.shift(7)
    df['lag_30'] = grupo.shift(30)

    # --- Médias móveis (shift(1) evita data leakage) ---
    df['rolling_mean_7']  = grupo.shift(1).rolling(7).mean()
    df['rolling_mean_30'] = grupo.shift(1).rolling(30).mean()
    df['rolling_std_7']   = grupo.shift(1).rolling(7).std()

    # --- Tendência: diferença entre lag_1 e lag_7 ---
    df['trend'] = df['lag_1'] - df['lag_7']

    df = df.dropna().reset_index(drop=True)

    print(f"Features criadas! Shape final: {df.shape}")
    print(f"   Colunas: {list(df.columns)}")
    return df
