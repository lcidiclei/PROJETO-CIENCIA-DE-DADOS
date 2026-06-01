def split_temporal(df, data_corte='2017-01-01'):
    train = df[df['date'] < data_corte]
    test = df[df['date'] >= data_corte]

    return train, test