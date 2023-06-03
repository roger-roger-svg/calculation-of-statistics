import pandas as pd

dados = [1.66,1.74,1.76,1.84,1.81,1.74,1.83,1.74]

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
