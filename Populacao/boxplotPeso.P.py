import matplotlib.pyplot as plt
import numpy as np

data = [np.array([60,120,64,74,70,90,78,116,65,66,80,65,51,75,72,96,88,80,60,75,72.5,95,58,75,60,71,67.5,75,72,56,69]),
       np.array([65,72,80,68,94,110,75,90,100,72.5,76,60,78,80]),
       np.array([75,69,85,79,67,70,67,57,115,73,75,62,75,98,80]),
       np.array([90,77,87,60,110,68,100,90,80]),
       np.array([64,70,95,60,62,60,90,77,140,90,101,110,125.])]


plt.boxplot(data)


plt.xlabel('modulos')
plt.ylabel('peso')
plt.title('Gráfico de Boxplot')

plt.show()