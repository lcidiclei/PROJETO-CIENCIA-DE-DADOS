import os
import urllib.request
import pandas as pd

DATASET_PATH = "train.csv"
URL_DATASET = ("https://www.kaggle.com/competitions/demand-forecasting-kernels-only/data?select=train.csv")

def baixar_dataset():
    print("Baixando dataset...")
    urllib.request.urlretrieve(
        URL_DATASET,
        DATASET_PATH
    )

def carregar_dataset(caminho):
    if os.path.exists(caminho):
        print("Dataset já existe.")
    else:
        baixar_dataset()

    df = pd.read_csv(caminho)
    print(f"Shape: {df.shape}")
    return df

df = carregar_dataset(DATASET_PATH)
