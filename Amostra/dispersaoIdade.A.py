import matplotlib.pyplot as plt

# Dados de exemplo
amostra = [
    ['Módulo 1', 32, 1.66, 65],
    ['Módulo 1', 18, 1.74, 80],
    ['Módulo 1', 19, 1.76, 60],
    ['Módulo 2', 30, 1.84, 90],
    ['Módulo 2', 33, 1.81, 94],
    ['Módulo 3', 30, 1.74, 75],
    ['Módulo 4', 21, 1.83, 110],
    ['Módulo 5', 26, 1.74, 64]
]

# Separar as variáveis "altura", "peso", "módulo" e "idade"
altura = [amostra[i][3] for i in range(len(amostra))]
idades = [amostra[i][1] for i in range(len(amostra))]

# Criar o gráfico de dispersão com o eixo x representando o módulo e o eixo y representando a idade
plt.scatter(altura, idades)

# Personalizar os rótulos dos eixos x e y e adicionar um título
plt.xlabel('peso')
plt.ylabel('Idade')
plt.title('Gráfico de Dispersão para a Variável Idade em Função do Módulo')

# Exibir o gráfico
plt.show()
