# Biblioteca para computação numérica, com suporte a arrays e operações matemáticas.
import numpy as np

# Biblioteca para manipulação e análise de dados, com estruturas como DataFrames e Series.
import pandas as pd

# Biblioteca para visualização de dados, com foco em gráficos estáticos e interativos.
import matplotlib.pyplot as plt

# Biblioteca de visualização baseada no Matplotlib, com gráficos estatísticos mais atraentes.
import seaborn as sns

# Carregando dataset e leitura do mesmo.
df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

df.shape
df.head()

# Renomeando as colunas com inplace=True para aplicar a mudança diretamente no DataFrame
df.rename(columns={'Time': 'Hora', 'Fatalities': 'Fatalidades'}, inplace=True)

# Removendo espaços extras nos nomes das colunas
df.columns = df.columns.str.strip()

# Convertendo 'Fatalidades' para numérico e criando a cópia com fatalidades > 0
df['Fatalidades'] = pd.to_numeric(df['Fatalidades'], errors='coerce')
df_fatalidades = df[df['Fatalidades'] > 0].copy()

# Calculando a média móvel para as fatalidades
df['Média Móvel Fatalidades'] = df['Fatalidades'].rolling(window=5).mean()

# Convertendo a coluna 'Hora' para datetime
df['Hora do Acontecimento'] = pd.to_datetime(df['Hora'], errors='coerce')

# Calculando a duração do voo em minutos
df['Duração do Voo (minutos)'] = df['Hora do Acontecimento'].dt.hour * 60 + df['Hora do Acontecimento'].dt.minute

# Selecionando os primeiros 25 registros para análise
df = df.head(25)

# Criando o gráfico de linhas
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Média Móvel Fatalidades", y="Hora do Acontecimento", marker="o")

# Ajustes básicos no gráfico
plt.xticks(rotation=45)
plt.xlabel("Média Móvel Fatalidades")
plt.ylabel("Hora do Acontecimento")
plt.title("Horário das Fatalidades")
plt.grid(True)

plt.show()
