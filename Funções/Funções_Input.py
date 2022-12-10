
# Minha ideia é aprender a utilizar inputs em funções para o usuário interagir, assim podemos criar até um projeto de calculadora

# Uma função para soma, nesse caso não utilizei parametros pq a ideia é deixar o usuário escolher
def soma():
    x = int(input("valor de x"))
    y = int(input("valor de y"))
    soma = x+y
    return soma

# O mesmo raciocinio anterior
def subtração():
    x = int(input("valor de x"))
    y = int(input("valor de y"))
    sub = x-y
    return sub


# Aqui eu criei um while para repetir a função a quantidade que eu achasse melhor
# i=0
# while(i < 1):
#     print("Escola uma opeação: 1 para soma e 2 para sub:")
#     opção = int(input("qual operação:"))
#     if opção == 1:
#         print("a soma de x e y é:", soma()) 
#     else:
#         print("a sub é", subtração())    
#     i+=1  

# Porém é melhor utilizar a estrutura While True e o usuário definir quando acabar
while True:
    # Variavel para sair do loop
    cont = 'S'
    print("Escola uma operação: 1 para soma e 2 para sub:")
    opção = int(input("qual operação:"))
    if opção == 1:
        print("a soma de x e y é:", soma()) 
    else:
        print("a sub é", subtração())
    # Pergunto se o usuário quer continuar, se a resposta for diferente de S, o programa terminará 
    cont = input("Deseja continuar? S|N") 
    if cont != 'S':
        print("Obrigado por participar")
        break       

