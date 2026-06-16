def sugerir_reabastecimento(modelo, df, dias_futuros=7, margem_seguranca=0.15):
    """
    Gera sugestão de quantidade a repor por loja/item.
    margem_seguranca: % extra sobre a previsão para evitar ruptura de estoque.
    """
    df_feat = criar_features(df)

    # Pega os dados mais recentes de cada loja/item
    ultimo_dia = df_feat.groupby(['store', 'item']).tail(1).copy()

    X_futuro = ultimo_dia[FEATURES]
    previsao = modelo.predict(X_futuro)
    previsao = np.clip(previsao, 0, None)

    ultimo_dia['previsao_diaria']  = previsao
    ultimo_dia['previsao_7dias']   = previsao * dias_futuros
    ultimo_dia['sugestao_repor']   = np.ceil(previsao * dias_futuros * (1 + margem_seguranca))

    resultado = ultimo_dia[['store', 'item', 'previsao_diaria', 'previsao_7dias', 'sugestao_repor']]
    resultado = resultado.sort_values(['store', 'item']).reset_index(drop=True)

    print(f"\nSugestão de Reabastecimento (próximos {dias_futuros} dias)")
    print(f"   Margem de segurança: {margem_seguranca*100:.0f}%")
    print()
    display(resultado.head(20))

    return resultado


if df is not None:
    reabastecimento = sugerir_reabastecimento(modelo, df)
