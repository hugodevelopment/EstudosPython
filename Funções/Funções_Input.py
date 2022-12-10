
# Minha ideia é aprender a utilizar inputs em funções para o usuário interagir, assim podemos criar até um projeto de calculadora
def soma():
    x = int(input("valor de x"))
    y = int(input("valor de y"))
    soma = x+y
    return soma

def subtração():
    x = int(input("valor de x"))
    y = int(input("valor de y"))
    sub = x-y
    return sub


# i=0
# while(i < 1):
#     print("Escola uma opeação: 1 para soma e 2 para sub:")
#     opção = int(input("qual operação:"))
#     if opção == 1:
#         print("a soma de x e y é:", soma()) 
#     else:
#         print("a sub é", subtração())    
#     i+=1  

while True:
    cont = 'S'
    print("Escola uma opeação: 1 para soma e 2 para sub:")
    opção = int(input("qual operação:"))
    if opção == 1:
        print("a soma de x e y é:", soma()) 
    else:
        print("a sub é", subtração())
    cont = input("Deseja continuar? S|N") 
    if cont != 'S':
        break       

