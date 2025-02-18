import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("../Airplane_Crashes_and_Fatalities_Since_1908.csv")

df.shape
df.head()

gp = df["Date"].value_counts()

gp = gp.reset_index()

gp = gp.rename(columns={"Date": "Data do acontecimento", "count": "Contagem"})

gp = gp.head(30)

sns.barplot(data=gp, x="Data do acontecimento", y="Contagem", width=0.8, color='red')

plt.title("Frequência de Acontecimentos por Data", fontsize=14, pad=20)

plt.xticks(rotation=90)
plt.yticks(rotation=50)

plt.tight_layout()

plt.show()