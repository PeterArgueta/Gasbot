import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('gasolina.csv')

# Seleccionar las columnas de fecha y kilómetros
fechas = pd.to_datetime(df['Fecha'])
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes'] = df['Fecha'].dt.to_period('M')
kilometros = df['Millas']
galones= df['Galones']

gasto_mensual= df.groupby('Mes')['Gasto'].sum()

gasto_total=df['Gasto'].sum()

#print(gasto_total)

mi_por_galon = kilometros / galones

fig, axs = plt.subplots(nrows=2, figsize=(10, 6))

axs[0].plot(fechas, mi_por_galon)
axs[0].set_ylabel('MPG')
axs[0].set_title('Consumo de Gasolina')
axs[0].grid(True)

gasto_mensual.plot(kind='bar', ax=axs[1])
axs[1].set_ylabel('Gasto mensual (Q)')
axs[1].set_xlabel(None)
axs[1].set_title('Gasto mensual de combustible')
axs[1].grid(True)

plt.tight_layout()
plt.show()

