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

gp = df
gp = gp.rename(columns={"Aboard": "Passageiros a bordo", "Fatalities": "Fatalidade"})

# Cria o gráfico de dispersão usando Seaborn
# data = conteúdo a ser tratado
# x = coluna x
# y = coluna y
# s = Tamanho das bolinhas que são de representatividade dos valores do gráfico
# alpha = Transparência
# color = cor das bolinhas que são de representatividade dos valores do gráfico
sns.scatterplot(data=gp, x='Passageiros a bordo', y='Fatalidade', s=100, alpha=0.7, color='red')

# Adiciona um título ao gráfico
plt.title("Relação entre passageiros a bordo e fatalidades", fontsize=14, pad=20)

# Ajusta o layout para evitar cortes nos rótulos
plt.tight_layout()

# Insere linhas guias
plt.grid(True)

# Exibe o gráfico
plt.show()