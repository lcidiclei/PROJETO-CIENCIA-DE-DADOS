import os
import urllib.request
import pandas as pd

DATASET_PATH = "train.csv"
URL_DATASET = ("https://www.kaggle.com/competitions/demand-forecasting-kernels-only/data?select=test.csv")

def baixar_dataset():


def carregar_dataset(caminho):
    if os.path.exists(DATASET_PATH):
        print("Dataset já existe.")
        return
      
    print("Baixando dataset...")
    urllib.request.urlretrieve(
        URL_DATASET,
        DATASET_PATH
    )

    if not os.path.exists(caminho):
        baixar_dataset()
      
    df = pd.read_csv(caminho)
    print(f"Shape: {df.shape}")
    return df

df = carregar_dataset(DATASET_PATH)
