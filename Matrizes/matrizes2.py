matriz = [ [0 for i in range(2)] for j in range(2)]
matriz_inversa = [ [0 for i in range(2)] for j in range(2)]
# count=0

for linha in range(2):
    for coluna in range(2):
        print("linha", linha)
        print("coluna", coluna)
        matriz[linha][coluna] = int(input("insira um numero"))
        matriz_inversa[0][0] = matriz[1][1]
        matriz_inversa[0][1] = -matriz[0][1]
        matriz_inversa[1][0] = -matriz[1][0]
        matriz_inversa[1][1] = matriz[0][0]
        # count += 1
    
for linha in range(2):
    for coluna in range(2):
        print("%5d" % matriz[linha][coluna], end='')
    print()

print("Calculando inversa")

for linha in range(2):
    for coluna in range(2):
        print("%5d" % matriz_inversa[linha][coluna], end='')    
    print()    

   