import matplotlib.pyplot as plt


def plot_resultados(y_test, pred):

    plt.figure(figsize=(12, 5))

    plt.plot(
        y_test.values[:200],
        label='Real'
    )

    plt.plot(
        pred[:200],
        label='Previsto'
    )

    plt.legend()

    plt.title("Real vs Previsto")

    plt.show()
