import matplotlib.pyplot as plt
import numpy as np


turma1 = np.array([19,31,20,19,23,18,31,22,32,20,18,33,47,21,25,19,17,31,19,25,26,32,23,28,25,19,39,34,18,21,34])
turma2 = np.array([28,33,31,22,33,34,19,30,42,26,27,25,40,23])
turma3 = np.array([19,23,43,21,21,27,21,22,26,28,30,26,22,24,33])
turma4 = np.array([34,33,32,21,21,26,26,27,20])
turma5 = np.array([26,23,30,30,23,22,26,27,43,19,29,21,26,0,0,0])


pesos = np.concatenate((turma1, turma2, turma3, turma4, turma5))


indices = np.arange(1,6)

media_pesos = np.mean(pesos.reshape(5, -1), axis=1)

media_predefinida = np.array([25,29.5,26,27,27])  #

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