import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("../Airplane_Crashes_and_Fatalities_Since_1908.csv")

df.shape
df.head()

df["Time"] = df["Time"].str.extract(r'(\d{1,2}:\d{2})')[0]

df["Hora do acontecimento"] = pd.to_datetime(df["Time"], format='%H:%M')
df["Data do acontecimento"] = pd.to_datetime(df["Date"]).dt.strftime('%d/%m/%Y')

df["Minutos do dia"] = df["Hora do acontecimento"].dt.hour * 60 + df["Hora do acontecimento"].dt.minute

df = df.head(25)

plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Data do acontecimento", y="Minutos do dia", marker="o")

plt.xticks(rotation=45)
plt.xlabel("Data")
plt.ylabel("Hora (minutos do dia)")
plt.title("Horário dos acontecimentos")
plt.grid(True)

plt.show()