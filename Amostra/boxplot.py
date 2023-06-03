import matplotlib.pyplot as plt


pesos = [65, 80, 60, 90, 94, 75, 110, 64]

# Criar o gráfico de boxplot
plt.boxplot(pesos)

# Personalizar os rótulos dos eixos x e y e adicionar um título
plt.xlabel('Peso')
plt.ylabel('Valores')
plt.title('Gráfico de Boxplot')

# Exibir o gráfico
plt.show()
