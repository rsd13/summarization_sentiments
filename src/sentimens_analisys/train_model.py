import pandas as pd
import os

def open_dataset():
    """
    función que abre el dataset
    :return: dataset en formato DataFrame
    """
    dir_path = os.path.dirname(os.path.abspath(__file__)) + "/../datasets/global_clean.csv"


    data = pd.read_csv(dir_path)
    print(data.isnull().sum())
    """
    data_null = data[data.frase.isnull()]
    data = data.drop(data_null.index)"""


open_dataset()
