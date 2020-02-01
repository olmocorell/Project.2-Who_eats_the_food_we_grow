import os
from dotenv import load_dotenv
import json
import requests
import re
import pandas as pd

def cargaDataSet():
    global data
    data = pd.read_csv("FAO.csv",encoding='cp1252')
    return data

def filtraPais():
    global datasp
    datasp = data[(data["Area"]== "Spain")]
    return datasp
