# Faça um script Python com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos através. 
# Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a primeira

# 1º Criar a função da soma com 3 argumentos:
def soma(x,y,z):
   soma = x+y+z
   return soma

# 2º Criar uma 2º função que calcula a média a partir da função soma()
def med(x,y,z):
    return soma(x,y,z)/3


# 3º Criar a função de menu para escolher os valores
def menu():
    x = int(input("escolha um numero:")) 
    y = int(input("escolha outro numero:"))
    z = int(input("escolha o ultimo numero"))
    print("A soma é", soma(x,y,z))
    print("A Media é",med(x,y,z))

# Inicializando o função menu
menu()
# opcao = True
# while(opcao):
#     cont = int(input("Deseja continuar 1 para sim e 2 para nao: 1|2"))
#     if(cont == 1):
#        menu()
#     else:
#         opcao = False

opcao = True
while(opcao):
    cont = str(input("Deseja continuar S para sim e N para nao: S|N"))
    print("teste",cont)
    if cont != "S":
        print("estou no if")
    else:
        print("estou aqui")