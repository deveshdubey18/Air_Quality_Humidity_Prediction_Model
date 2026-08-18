import numpy as np
import pandas as pd


def loader():
    df = pd.read_excel(r'https://github.com/deveshdubey18/Air_Quality_Humidity_Prediction_Model/raw/refs/heads/main/data/AirQualityUCI.xlsx')
    return df

