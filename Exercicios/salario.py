# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

resposta =""

while resposta !='N':

    salario = int(input("Qual é o seu salario ?"))

    perc = 0.15

    novo_salario = salario + (salario *perc)

    resposta = input("Deseja continuar S|N")
    
       
                  

print(novo_salario)