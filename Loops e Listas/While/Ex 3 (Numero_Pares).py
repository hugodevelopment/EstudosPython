# Ex: Crie um programa que peça um número ao usuário e imprima todos os números pares de 1 até o número fornecido"
# Como resolver: Criar um loop while para finalizar quando chegar ao número escolhido pelo usuário

numero_user = int(input("Digite um numero de 1 a 100:"))

count = 1

while count <= numero_user:
    if(count % 2 == 0):
       print("Os numeros pares são", count)
    count+=1      