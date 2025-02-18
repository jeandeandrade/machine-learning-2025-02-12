import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

df.shape
df.head()

df.rename(columns={'Time': 'Hora', 'Fatalities': 'Fatalidades'}, inplace=True)

df.columns = df.columns.str.strip()

df['Fatalidades'] = pd.to_numeric(df['Fatalidades'], errors='coerce')
df_fatalidades = df[df['Fatalidades'] > 0].copy()

df['Média Móvel Fatalidades'] = df['Fatalidades'].rolling(window=5).mean()

df['Hora do Acontecimento'] = pd.to_datetime(df['Hora'], errors='coerce')

df['Duração do Voo (minutos)'] = df['Hora do Acontecimento'].dt.hour * 60 + df['Hora do Acontecimento'].dt.minute

df = df.head(25)

plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Média Móvel Fatalidades", y="Hora do Acontecimento", marker="o")

plt.xticks(rotation=45)
plt.xlabel("Média Móvel Fatalidades")
plt.ylabel("Hora do Acontecimento")
plt.title("Horário das Fatalidades")
plt.grid(True)

plt.show()