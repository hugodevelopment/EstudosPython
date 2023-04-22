linhas = [1]
coluna = [[3,1], 
          [2,-1],]
i = 0
for i in range(len(linhas)):
    for j in coluna:
        i += 1
        # print(i,coluna[1][1])
        delta = coluna[0][1] * coluna[1][1]
    print(delta)  


# def criar_matriz(n_linhas, n_colunas):
#     matriz = []
#     for i in range(n_linhas):
#         linha = []
#         for j in range(n_colunas):
#             linha.append(0)  # preenche a linha com zeros
#             matriz.append(linha)  # adiciona a linha à matriz
#     return matriz

# print(criar_matriz(3,2))

