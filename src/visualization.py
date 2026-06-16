import matplotlib.pyplot as plt

def plot_resultados(y_test, pred, test_df, resultados):
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle('Resultados do Modelo de Previsão de Demanda', fontsize=16, fontweight='bold')

    # 1. Real vs Previsto (primeiras 200 amostras)
    axes[0, 0].plot(y_test.values[:200], label='Real', linewidth=1.5, color='steelblue')
    axes[0, 0].plot(pred[:200], label='Previsto', linewidth=1.5, color='coral', linestyle='--')
    axes[0, 0].set_title('Real vs Previsto (primeiras 200 amostras)')
    axes[0, 0].set_xlabel('Amostras')
    axes[0, 0].set_ylabel('Vendas')
    axes[0, 0].legend()

    # 2. Comparação de métricas entre modelos
    nomes  = list(resultados.keys())
    smapes = [resultados[n]['SMAPE'] for n in nomes]
    bars = axes[0, 1].bar(nomes, smapes, color=['steelblue', 'coral', 'mediumseagreen'])
    axes[0, 1].set_title('SMAPE por Modelo (menor = melhor)')
    axes[0, 1].set_ylabel('SMAPE (%)')
    for bar, val in zip(bars, smapes):
        axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                       f'{val:.2f}%', ha='center', va='bottom', fontweight='bold')

    # 3. Distribuição dos resíduos
    residuos = y_test.values - pred
    axes[1, 0].hist(residuos, bins=50, color='mediumpurple', edgecolor='white')
    axes[1, 0].axvline(0, color='red', linestyle='--', linewidth=1.5)
    axes[1, 0].set_title('Distribuição dos Resíduos')
    axes[1, 0].set_xlabel('Erro (Real - Previsto)')
    axes[1, 0].set_ylabel('Frequência')

    # 4. Real vs Previsto (scatter)
    axes[1, 1].scatter(y_test.values[:500], pred[:500], alpha=0.3, color='steelblue', s=10)
    lim = max(y_test.values[:500].max(), pred[:500].max())
    axes[1, 1].plot([0, lim], [0, lim], 'r--', linewidth=1.5, label='Perfeito')
    axes[1, 1].set_title('Scatter: Real vs Previsto')
    axes[1, 1].set_xlabel('Real')
    axes[1, 1].set_ylabel('Previsto')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.show()
