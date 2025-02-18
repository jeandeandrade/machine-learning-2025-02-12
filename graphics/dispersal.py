import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("../Airplane_Crashes_and_Fatalities_Since_1908.csv")

df.shape
df.head()

gp = df
gp = gp.rename(columns={"Aboard": "Passageiros a bordo", "Fatalities": "Fatalidade"})

sns.scatterplot(data=gp, x='Passageiros a bordo', y='Fatalidade', s=100, alpha=0.7, color='red')

plt.title("Relação entre passageiros a bordo e fatalidades", fontsize=14, pad=20)

plt.tight_layout()

plt.grid(True)

plt.show()