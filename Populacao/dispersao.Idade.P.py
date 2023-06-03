import matplotlib.pyplot as plt

# Dados de exemplo
amostra = [
['Módulo 3',19,1.76,75],
['Módulo 3',23,1.92,69],
['Módulo 3',43,1.7,85],
   ['Módulo 3', 21, 1.75, 79],
   ['Módulo 2', 28, 1.7, 65],
   ['Módulo 5', 26, 1.74, 64],
['Módulo 3', 21, 1.6, 67],
['Módulo 2', 33, 1.71, 72],
['Módulo 2', 31, 1.65, 80],
['Módulo 3', 27, 1.73, 70],
['Módulo 3', 21, 1.78, 67],
['Módulo 3', 22, 1.8, 57],
['Módulo 5', 23, 1.7, 70],
['Módulo 5', 30, 1.78, 95],
['Módulo 5', 30, 1.72, 60],
['Módulo 2', 22, 1.8, 68],
['Módulo 5', 23, 1.68, 62],
['Módulo 5', 22, 1.72, 60],
['Módulo 5', 26, 1.73, 90],
['Módulo 3', 26, 1.8, 115],
['Módulo 5', 27, 1.66, 77],
['Módulo 1', 39, 1.71, 67.5],
['Módulo 1', 34, 1.77, 75],
['Módulo 1', 18, 1.77, 72],
['Módulo 3', 28, 1.66, 73],
['Módulo 3', 30, 1.74, 75],
['Módulo 3', 26, 1.65, 62],
['Módulo 3', 22, 1.83, 75],
['Módulo 1', 31, 1.7, 80],
['Módulo 1', 19, 1.76, 60],
['Módulo 1', 25, 1.78, 75],
['Módulo 1', 26, 1.75, 72.5],
['Módulo 1', 32, 1.75, 95],
['Módulo 1', 23, 1.75, 58],
['Módulo 1', 28, 1.65, 75],
['Módulo 1', 25, 1.75, 60],
['Módulo 1', 19, 1.72, 71],
['Módulo 4', 34, 1.92, 90],
['Módulo 4', 33, 1.62, 77],
['Módulo 1', 17, 1.73, 88],
['Módulo 4', 32, 1.86, 87],
['Módulo 3', 24, 1.75, 98],
['Módulo 5', 43, 1.81, 140],
['Módulo 4', 21, 1.79, 60],
['Módulo 1', 25, 1.8, 72],
['Módulo 1', 25, 1.8, 72],
['Módulo 1', 19, 1.73, 96],
['Módulo 5', 19, 1.78, 90],
['Módulo 1', 19, 1.8, 60],
['Módulo 1', 31, 1.83, 120],
['Módulo 1', 20, 1.65, 64],
['Módulo 1', 19, 1.9, 74],
['Módulo 1', 23, 1.73, 70],
['Módulo 1', 18, 2.00, 90],
['Módulo 1', 31, 1.75, 78],
['Módulo 1', 22, 1.92, 116],
['Módulo 1', 32, 1.66, 65],
['Módulo 1', 20, 1.75, 66],
['Módulo 1', 18, 1.74, 80],
['Módulo 1', 33, 1.76, 65],
['Módulo 1', 47, 1.63, 51],
['Módulo 1', 21, 1.75, 75],
['Módulo 2', 33, 1.81, 94],
['Módulo 2', 34, 1.87, 110],
['Módulo 2', 19, 1.7, 75],
['Módulo 2', 30, 1.84, 90],
['Módulo 2', 42, 1.78, 100],
['Módulo 2', 26, 1.79, 72.5],
['Módulo 1', 21, 1.72, 56],
['Módulo 1', 34, 1.75, 69],
['Módulo 5', 29, 1.81, 101],
['Módulo 5', 21, 1.9, 110],
['Módulo 2', 19, 1.75, 67],
['Módulo 5', 26, 1.81, 125],
['Módulo 2', 27, 1.77, 76],
['Módulo 2', 25, 1.60, 60],
['Módulo 2', 40, 1.74, 78],
['Módulo 2', 23, 1.7, 80],
['Módulo 4', 21, 1.83, 110],
['Módulo 4', 26, 1.87, 68],
['Módulo 4', 26, 1.82, 100],
['Módulo 4', 27, 1.82, 90],
['Módulo 4', 20, 1.75, 80],
['Módulo 4', 33, 1.72, 80]


]

# Separar as variáveis "altura" e "peso"
peso = [amostra[i][3] for i in range(len(amostra))]
idade = [amostra[i][1] for i in range(len(amostra))]

# Criar o gráfico de dispersão
plt.scatter(peso, idade)

# Personalizar os rótulos dos eixos x e y e adicionar um título
plt.xlabel('peso')
plt.ylabel('idade')
plt.title('Gráfico de Dispersão para a Variável Altura em Função da idade')

# Exibir o gráfico
plt.show()
