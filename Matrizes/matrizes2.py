matriz = [ [0 for i in range(2)] for j in range(4)]
# count=0

for linha in range(4):
    for coluna in range(4):
        print("linha", linha)
        print("coluna", coluna)
        matriz[linha][coluna] = int(input("insira um numero"))
        # count += 1
    
for linha in range(4):
    for coluna in range(3):
        print("%5d" % matriz[linha][coluna], end='')
    print()
