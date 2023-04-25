
coluna = [[3,1], 
          [2,-1]]

for i in range(1):
    for j in coluna:
        print(j)
        delta = coluna[0][0] * coluna[1][1] - coluna[1][0] * coluna[0][1]
    print(delta)  
    if delta != 0:
        print("A matriz tem inversa")
        inversa = 1/delta 
        print(inversa)     
    else:
        print("A matriz não pode ter inversa já que ", delta, "é" , "0")


# def criar_matriz(n_linhas, n_colunas):
#     matriz = []
#     for i in range(n_linhas):
#         linha = []
#         for j in range(n_colunas):
#             linha.append(0)  # preenche a linha com zeros
#             matriz.append(linha)  # adiciona a linha à matriz
#     return matriz

# print(criar_matriz(3,2))

