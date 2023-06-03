import pandas as pd

dados = [
75,
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
        80
]

df = pd.DataFrame(dados, columns=['Valores'])
tabela = df['Valores'].value_counts().reset_index()
tabela.columns = ['xi', 'fi']

tabela = tabela.sort_values('xi').reset_index(drop=True)
tabela['li'] = tabela.index + 1
tabela['LI'] = tabela['li'] - 0.5
tabela['%fr'] = tabela['fi'] / len(dados) * 100
tabela['fac'] = tabela['fi'].cumsum()
tabela['%frc'] = tabela['fac'] / len(dados) * 100
tabela['fad'] = len(dados) - tabela['fac'].shift(1).fillna(0)
tabela['%frd'] = tabela['fad'] / len(dados) * 100

print(tabela)
