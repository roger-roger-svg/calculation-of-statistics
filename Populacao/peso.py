# --- DADOS COLETADOS ---
dados = [75,
        69,
        85,
        79,
        65,
        64,
        67,
        72,
        80,
        70,
        67,
        57,
        70,
        95,
        60,
        68,
        62,
        60,
        90,
        115,
        77,
        67.5,
        75,
        72,
        73,
        75,
        62,
        75,
        80,
        60,
        75,
        72.5,
        95,
        58,
        75,
        60,
        71,
        90,
        77,
        88,
        87,
        98,
        140,
        60,
        72,
        96,
        90,
        60,
        120,
        64,
        74,
        70,
        90,
        78,
        116,
        65,
        66,
        80,
        65,
        51,
        75,
        94,
        110,
        75,
        90,
        100,
        72.5,
        56,
        69,
        101,
        110,
        67,
        125,
        76,
        60,
        78,
        80,
        110,
        68,
        100,
        90,
        80,
        80]

# --- BIBLIOTECAS IMPORTADAS ---
import statistics as s
import math as m

# --- FUNÇÕES ---
def media(lista):
    media = m.ceil(s.mean(lista))
    return media

def moda(lista):
    moda = s.mode(lista)
    return moda

def mediana(lista):
    mediana = s.median(lista)
    return mediana

def desvio_padrao(lista):
    dv = m.ceil(s.stdev(lista))
    return dv

def coef_variacao(lista):
    cv = m.ceil((desvio_padrao(lista)/media(lista)) * 100)
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
print("*** ANALISE DE DADOS DAS PESOS ***")
print("Media:", media(dados))
print("Moda:", moda(dados))
print("Mediana:", mediana(dados))
print("Desvio padrao:", desvio_padrao(dados))
print("Coeficiente de variacao:", coef_variacao(dados))
print("Variancia amostral:", variancia(dados))
print("Amplitude:", amplitude(dados))

print("\nQuartil 1, 2 e 3:", quartil())
homogeneidade()