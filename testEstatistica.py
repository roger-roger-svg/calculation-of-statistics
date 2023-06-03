import statistics


entrada = input("Digite os dados separados por vírgulas: ")


dados_str = entrada.split(",")
dados = [1.76,
        1.92,
        1.70,
        1.75,
        1.70,
        1.74,
        1.60,
        1.71,
        1.65,
        1.73,
        1.78,
        1.80,
        1.70,
        1.78,
        1.72,
        1.80,
        1.68,
        1.72,
        1.73,
        1.80,
        1.66,
        1.71,
        1.77,
        1.77,
        1.66,
        1.74,
        1.65,
        1.83,
        1.70,
        1.76,
        1.78,
        1.75,
        1.75,
        1.75,
        1.65,
        1.75,
        1.72,
        1.92,
        1.62,
        1.73,
        1.86,
        1.75,
        1.81,
        1.79,
        1.80,
        1.73,
        1.78,
        1.80,
        1.83,
        1.65,
        1.90,
        1.73,
        2.00,
        1.75,
        1.92,
        1.66,
        1.75,
        1.74,
        1.76,
        1.63,
        1.75,
        1.81,
        1.87,
        1.70,
        1.84,
        1.78,
        1.79,
        1.72,
        1.75,
        1.81,
        1.90,
        1.75,
        1.81,
        1.77,
        1.60,
        1.74,
        1.70,
        1.83,
        1.87,
        1.82,
        1.82,
        1.75,
        1.72]
for valor_str in dados_str:
    try:
        valor = float(valor_str)
        dados.append(valor)
    except ValueError:
        print("Valor inválido:", valor_str)


media = statistics.mean(dados)
moda = statistics.mode(dados)
mediana = statistics.median(dados)
desvio_padrao = statistics.stdev(dados)
coef_variacao = (desvio_padrao / media) * 100
variancia = statistics.variance(dados)
amplitude = max(dados) - min(dados)


dados_ordenados = sorted(dados)
n = len(dados_ordenados)
quartil_1 = statistics.median(dados_ordenados[:n//2])
quartil_2 = statistics.median(dados_ordenados)
quartil_3 = statistics.median(dados_ordenados[(n+1)//2:])


if coef_variacao <= 15:
    homogeneidade = "Os dados são considerados homogêneos."
elif coef_variacao >= 30:
    homogeneidade = "Os dados são considerados heterogêneos."
else:
    homogeneidade = "Os dados são considerados neutros."

# Exibe os resultados
print("Média:", media)
print("Moda:", moda)
print("Mediana:", mediana)
print("Desvio padrão amostral:", desvio_padrao)
print("Coeficiente de variação:", coef_variacao, "%")
print(homogeneidade)
print("Variância amostral:", variancia)
print("Amplitude:", amplitude)
print("Quartil 1:", quartil_1)
print("Quartil 2:", quartil_2)
print("Quartil 3:", quartil_3)

