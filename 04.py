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

df.rename(columns={'Time': 'Hora', 'Fatalities': 'Fatalidades'}, inplace=True)
df['Fatalidades'] = pd.to_numeric(df['Fatalidades'], errors='coerce')
df_fatalidades = df[df['Fatalidades'] > 0].copy()


# Comparando o número de registros
print("Número de registros no dataset original:", df.shape[0])
print("Número de registros no dataset filtrado:", df_fatalidades.shape[0])

# Comparando estatísticas descritivas
print("\nEstatísticas descritivas do dataset original:")
print(df.describe())

print("\nEstatísticas descritivas do dataset filtrado:")
print(df_fatalidades.describe())

# Visualizando as distribuições de Fatalidades no dataset original e filtrado
plt.figure(figsize=(12, 6))

# Distribuição das Fatalidades no dataset original
plt.subplot(1, 2, 1)
sns.histplot(df['Fatalidades'], kde=True, color='blue', bins=30)
plt.title('Distribuição de Fatalidades (Original)')
plt.xlabel('Fatalidades')
plt.ylabel('Frequência')

# Distribuição das Fatalidades no dataset filtrado
plt.subplot(1, 2, 2)
sns.histplot(df_fatalidades['Fatalidades'], kde=True, color='red', bins=30)
plt.title('Distribuição de Fatalidades (Filtrado - >0)')
plt.xlabel('Fatalidades')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()
