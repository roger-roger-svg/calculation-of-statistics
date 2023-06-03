# --- DADOS COLETADOS ---
dados = [1.66,1.74,1.76,1.84,1.81,1.74,1.83,1.74]

# --- BIBLIOTECAS IMPORTADAS ---
import statistics as s
import math as m


# --- FUNÇÕES ---



def moda(lista):
    moda = s.mode(lista)
    return moda
def media(lista):
    media = (s.mean(lista))
    return media

def mediana(lista):
    mediana = s.median(lista)
    return mediana


def desvio_padrao(lista):
    dv = m.ceil(s.stdev(lista))
    return dv


def coef_variacao(lista):
    cv = m.ceil((desvio_padrao(lista) / media(lista)) * 100)
    return cv


def variancia(lista):
    variancia = m.ceil(s.variance(lista))
    return variancia


def amplitude(lista):
    amp = m.ceil(max(lista) - min(lista))
    return amp


def quartil():
    dados_ordenados = sorted(dados)
    tamanho = len(dados_ordenados)

    quartil_Um = s.median(dados_ordenados[:tamanho // 2])
    quartil_Dois = s.median(dados_ordenados)
    quartil_Tres = s.median(dados_ordenados[(tamanho + 1) // 2:])

    return quartil_Um, quartil_Dois, quartil_Tres


def homogeneidade():
    if coef_variacao(dados) <= 15:
        print("Os dados sao considerados homogeneos.")
    elif coef_variacao(dados) >= 30:
        print("Os dados sao considerados heterogeneos.")
    else:
        print("Os dados sao considerados neutros.")


# --- --- ---

# --- FUNCIONAMENTO ---
print("*** ANALISE DE DADOS DAS ALTURAS ***")
print("Media:", media(dados))
print("Moda:", moda(dados))
print("Mediana:", mediana(dados))
print("Desvio padrao:", desvio_padrao(dados))
print("Coeficiente de variacao:", coef_variacao(dados))
print("Variancia amostral:", variancia(dados))
print("Amplitude:", amplitude(dados))

print("\nQuartil 1, 2 e 3:", quartil())
homogeneidade()