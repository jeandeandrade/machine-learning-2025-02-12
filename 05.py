import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")
df.shape

df["Year"] = pd.to_datetime(df["Date"]).dt.strftime('%Y')
df.head()