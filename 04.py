import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

df.shape
df.head()

df.rename(columns={'Time': 'Hora', 'Fatalities': 'Fatalidades'}, inplace=True)
df['Fatalidades'] = pd.to_numeric(df['Fatalidades'], errors='coerce')
df_fatalidades = df[df['Fatalidades'] > 0].copy()

print("Número de registros no dataset original:", df.shape[0])
print("Número de registros no dataset filtrado:", df_fatalidades.shape[0])

print("\nEstatísticas descritivas do dataset original:")
print(df.describe())

print("\nEstatísticas descritivas do dataset filtrado:")
print(df_fatalidades.describe())

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['Fatalidades'], kde=True, color='blue', bins=30)
plt.title('Distribuição de Fatalidades (Original)')
plt.xlabel('Fatalidades')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.histplot(df_fatalidades['Fatalidades'], kde=True, color='red', bins=30)
plt.title('Distribuição de Fatalidades (Filtrado - >0)')
plt.xlabel('Fatalidades')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()