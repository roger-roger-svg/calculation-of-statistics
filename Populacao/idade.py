# --- DADOS COLETADOS ---
dados = [19,
        23,
        43,
        21,
        28,
        26,
        21,
        33,
        31,
        27,
        21,
        22,
        23,
        30,
        30,
        22,
        23,
        22,
        26,
        26,
        27,
        39,
        34,
        18,
        28,
        30,
        26,
        22,
        31,
        19,
        25,
        26,
        32,
        23,
        28,
        25,
        19,
        34,
        33,
        17,
        32,
        24,
        43,
        21,
        25,
        19,
        19,
        19,
        31,
        20,
        19,
        23,
        18,
        31,
        22,
        32,
        20,
        18,
        33,
        47,
        21,
        33,
        34,
        19,
        30,
        42,
        26,
        21,
        34,
        29,
        21,
        19,
        26,
        27,
        25,
        40,
        23,
        21,
        26,
        26,
        27,
        20,
        33]

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
print("*** ANALISE DE DADOS DAS IDADES ***")
print("Media:", media(dados))
print("Moda:", moda(dados))
print("Mediana:", mediana(dados))
print("Desvio padrao:", desvio_padrao(dados))
print("Coeficiente de variacao:", coef_variacao(dados))
print("Variancia amostral:", variancia(dados))
print("Amplitude:", amplitude(dados))

print("\nQuartil 1, 2 e 3:", quartil())
homogeneidade()