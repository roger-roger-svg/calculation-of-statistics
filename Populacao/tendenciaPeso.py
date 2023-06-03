import matplotlib.pyplot as plt
import numpy as np


turma1 = np.array([60,120,64,74,70,90,78,116,65,66,80,65,51,75,72,96,88,80,60,75,72.5,95,58,75,60,71,67.5,75,72,56,69])
turma2 = np.array([65,72,80,68,94,110,75,90,100,72.5,76,60,78,80])
turma3 = np.array([75,69,85,79,67,70,67,57,115,73,75,62,75,98,80])
turma4 = np.array([90,77,87,60,110,68,100,90,80])
turma5 = np.array([64,70,95,60,62,60,90,77,140,90,101,110,125,0,0,0])


pesos = np.concatenate((turma1, turma2, turma3, turma4, turma5))


indices = np.arange(1,6)

media_pesos = np.mean(pesos.reshape(5, -1), axis=1)

media_predefinida = np.array([75, 80, 76, 85, 88])  # Definindo a média predefinida

erro = np.std(pesos.reshape(5, -1), axis=1)  # calculando o desvio padrão

z = np.polyfit(indices, media_predefinida, 1)  # ajustando a linha de tendência com a média predefinida
p = np.poly1d(z)

trend_x = np.linspace(np.min(indices), np.max(indices), 100)

trend_y = p(trend_x)

plt.bar(indices, media_pesos,  capsize=5, ecolor='black', alpha=0.5)
plt.plot(trend_x, trend_y, "r--")
plt.title("Gráfico de Barras de Tendência")
plt.xlabel("Turma")
plt.ylabel("Peso Médio (kg)")
plt.show()




