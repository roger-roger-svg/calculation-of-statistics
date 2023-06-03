import matplotlib.pyplot as plt
import numpy as np


turma1 = np.array([1.8,1.83,1.65,1.9,1.73,2,1.75,1.92,1.66,1.75,1.74,1.76,1.63,1.75,1.8,1.73,1.73,1.7,1.76,1.78,1.75,1.75,1.75,1.65,1.75,1.72,1.71,1.77,1.77,1.72,1.75])
turma2 = np.array([1.7,1.71,1.65,1.8,1.81,1.87,1.7,1.84,1.78,1.79,1.77,1.6,1.74,1.7])
turma3 = np.array([1.76,1.92,1.7,1.75,1.6,1.73,1.78,1.8,1.8,1.66,1.74,1.65,1.83,1.75,1.72])
turma4 = np.array([1.92,1.62,1.86,1.79,1.83,1.87,1.82,1.82,1.75])
turma5 = np.array([1.74,1.7,1.78,1.72,1.68,1.72,1.73,1.66,1.81,1.78,1.81,1.9,1.81,0,0,0])


pesos = np.concatenate((turma1, turma2, turma3, turma4, turma5))


indices = np.arange(1,6)

media_pesos = np.mean(pesos.reshape(5, -1), axis=1)

media_predefinida = np.array([1.76, 1.75, 1.74, 1.81, 1.76])  #

erro = np.std(pesos.reshape(5, -1), axis=1)

z = np.polyfit(indices, media_predefinida, 1)
p = np.poly1d(z)

trend_x = np.linspace(np.min(indices), np.max(indices), 100)

trend_y = p(trend_x)

plt.bar(indices, media_pesos,  capsize=5, ecolor='black', alpha=0.5)
plt.plot(trend_x, trend_y, "r--")
plt.title("Gráfico de Barras de Tendência")
plt.xlabel("Turma")
plt.ylabel("")
plt.show()