# 1º Criar uma lista com dos valores para calcular a média
# 2º Utilizar o for para percorrer a lista e fazer os calculos de média


import numpy as np

dados = [8.28,8.22,8.29,8.25,8.26,8.26,8.26,8.23,8.30,8.27]
media = np.mean(dados)
desvio_padrão = np.std(dados)
print(media)
print(desvio_padrão)

soma = 0
for i in dados:
    soma = soma + i
media = soma/len(dados)
print(media)

