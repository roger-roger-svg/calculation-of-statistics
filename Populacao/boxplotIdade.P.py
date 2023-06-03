import matplotlib.pyplot as plt
import numpy as np

data = [np.array([19,31,20,19,23,18,31,22,32,20,18,33,47,21,25,19,17,31,19,25,26,32,23,28,25,19,39,34,18,21,34]),
       np.array([28,33,31,22,33,34,19,30,42,26,27,25,40,23]),
       np.array([19,23,43,21,21,27,21,22,26,28,30,26,22,24,33]),
       np.array([34,33,32,21,21,26,26,27,20]),
       np.array([26,23,30,30,23,22,26,27,43,19,29,21,26.])]

plt.boxplot(data)
plt.title("Exemplo de 5 boxplots de idade ")
plt.xlabel("modulos")
plt.ylabel("idades")
plt.show()
