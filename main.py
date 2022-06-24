import pandas as pd
import numpy as np
import requests
from data_handler.data import data_handler
import pickle


def data():
    url = "https://raw.githubusercontent.com/Biswajit7890/Data-Storage/main/cars.json"
    dict_list = data_handler(url)
    with open("parrot.pkl", "wb") as f:
        pickle.dump(dict_list, f)


if __name__ == __main__:
    data()

