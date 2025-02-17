# Biblioteca para computação numérica, com suporte a arrays e operações matemáticas.
import numpy as np

# Biblioteca para manipulação e análise de dados, com estruturas como DataFrames e Series.
import pandas as pd

# Biblioteca para visualização de dados, com foco em gráficos estáticos e interativos.
import matplotlib.pyplot as plt

# Biblioteca de visualização baseada no Matplotlib, com gráficos estatísticos mais atraentes.
import seaborn as sns

# Carregando dataset e leitura do mesmo.
df = pd.read_csv("../Airplane_Crashes_and_Fatalities_Since_1908.csv")

df.shape
df.head()

df["Time"] = df["Time"].str.extract(r'(\d{1,2}:\d{2})')[0]

# Convertendo colunas para os formatos corretos
df["Hora do acontecimento"] = pd.to_datetime(df["Time"], format='%H:%M')
df["Data do acontecimento"] = pd.to_datetime(df["Date"]).dt.strftime('%d/%m/%Y')

# Convertendo horário para minutos do dia
df["Minutos do dia"] = df["Hora do acontecimento"].dt.hour * 60 + df["Hora do acontecimento"].dt.minute

df = df.head(25)

# Criando o gráfico de linhas
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Data do acontecimento", y="Minutos do dia", marker="o")

# Ajustes básicos
plt.xticks(rotation=45)
plt.xlabel("Data")
plt.ylabel("Hora (minutos do dia)")
plt.title("Horário dos acontecimentos")
plt.grid(True)

plt.show()