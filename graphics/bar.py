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

# Conta a frequência de cada valor único na coluna "Date" e retorna uma série com os resultados.
gp = df["Date"].value_counts()
#gp = df.groupby('Date').value_counts(ascending=False)

# print(gp)

# Converte a série em um DataFrame, onde "index" será a coluna com as datas e "count" será a coluna com as contagens.
gp = gp.reset_index()


# Renomeia as colunas do DataFrame antes de fazer o gráfico:
gp = gp.rename(columns={"Date": "Data do acontecimento", "count": "Contagem"})

# Limita os dados aos 25 primeiros registros (para evitar sobrecarregar o gráfico).
gp = gp.head(30)

# Formata as datas para exibir o dia/mês/ano.
gp["Data do acontecimento"] = pd.to_datetime(gp["Data do acontecimento"]).dt.strftime('%d/%m/%Y') # Formato dia/mês/ano

# Cria um gráfico de barras usando Seaborn
# Utilizar width para manipulação do tamanho das barras, e trazer assim mais dados
sns.barplot(data=gp, x="Data do acontecimento", y="Contagem", width=0.8, color='red')

# Adiciona um título ao gráfico usando Matplotlib.
plt.title("Frequência de Acontecimentos por Data", fontsize=14, pad=20)

# Rotaciona os rótulos do eixo X em 90 graus para melhorar a legibilidade.
plt.xticks(rotation=90)
plt.yticks(rotation=50)

# Ajusta o layout para evitar cortes nos rótulos.
plt.tight_layout()

# Exibe o gráfico.
plt.show()