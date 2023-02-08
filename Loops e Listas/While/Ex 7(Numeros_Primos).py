# Criando as variaveis para utilizar o programa
n = n_ = int(input('Número: '))
# Lista para o numero de divisores, lembrando que um numero primo tem apenas ele mesmo e 1 como divisores
n_divisores = []
# Lista para receber os numeros primos
primos = []

# Funão para preencher a lista apenas com os divisores primos
def divisores(x,y):
     if x%y==0:
        n_divisores.append(y)
        print(n_divisores)

while True:
    if n == 1:
        break
    # For que vai de n, até 0, subtraindo 1: 15-1, 14-1
    for i in range(n, 0, -1):
        # Chamando a função divisores
        divisores(n,i)
    #Se o número de divisores for igual a n e 1 é primo 
    if n_divisores == [n, 1]:
        primos.append(n)
    #Descrescendo 
    n -= 1
    # Esvaizando a lista para cada numero no intervalo
    n_divisores = []

print(f'Os números primos presentes no intervalo {n_} - 0 são: ', end='')
for nums in primos:
    if nums != primos[-1]:
        print(nums, end=', ')
    else:
        print(nums, end='.')

        
# i=0
# while i < len(primos):
#     print(primos[-1])
#     if i != primos[-1]:
#         print(primos[i], end=',')
#     else:
#         print(primos[i], end='.')
#     i += 1
 