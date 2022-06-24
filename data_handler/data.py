import pandas as pd
import numpy as np
import requests
import os
import logging
import json
from collections import defaultdict


# Defining all the logger functions also the log file which will catching all the information and Exception

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler("data_transform.log", mode="w")
fileHandler.setLevel(logging.INFO)
fileFormat = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fileHandler.setFormatter(fileFormat)
logger.addHandler(fileHandler)


data_list = []


def data_handler(infile):
    try:
        resp = requests.get(infile)
        data = json.loads(resp.text)
        for i in range(len(data)):
            for a, b in data[i].items():
                data_set = {"key": a, "val": b}
                data_list.append(data_set)
        raise NotImplementedError
    except Exception as e:
        logger.error(e)
    return data_list

