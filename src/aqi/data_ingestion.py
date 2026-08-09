import numpy as np
import pandas as pd


def loader():
    df = pd.read_excel(r'C:\AQI\data\AirQualityUCI.xlsx')
    return df

